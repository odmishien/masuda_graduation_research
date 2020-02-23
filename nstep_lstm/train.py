import os
import re
import argparse
import pickle
from gensim.models import word2vec
import numpy
import chainer
from chainer import optimizers, serializers, iterators, training
from chainer.backends import cuda
from chainer.training import extensions

from SimpleLSTM import SimpleLSTM


def parse_arg():
    parser = argparse.ArgumentParser(description='LSTM')
    parser.add_argument('-e', '--epoch', type=int, default=100,
                        help='the training epochs.')
    parser.add_argument('-b', '--batch_size', type=int, default=20,
                        help='batch size.')
    parser.add_argument('-s', '--save_interval', type=int, default=100,
                        help='save models at every specified interval of the epoch.')
    parser.add_argument('-g', '--gpuid', type=int, default=-1,
                        help='GPU ID (negative value indicates CPU)')
    parser.add_argument('-o', '--output_dir', type=str, default='.',
                        help='all output will be stored in the specified output directory.')
    parser.add_argument('-r', '--resume_from_snapshot', type=str,
                        help='resume training from specified snapshot.')
    parser.add_argument('-n', '--n_hidden', type=int, default=200,
                        help='the number of hidden neurons in LSTM.')
    parser.add_argument('-l', '--n_layers', type=int, default=1,
                        help='the number of layers of LSTM.')
    return parser.parse_args()


def setup_train_data(gpuid=-1):
    if 0 <= gpuid:
        xp = cuda.cupy
    else:
        xp = numpy
    x_list = []
    y_list = []
    keys = []
    delete_entries = []

    model = word2vec.Word2Vec.load("../masuda.model_20181218")
    with open('../pickle/masuda_hotentry','rb') as p:
        masuda = pickle.load(p)
    # エントリーをベクトルに変換する
    entries = os.listdir("../hotentries")
    arrays_2 = [(re.search("[0-9]+", x).group(), x) for x in entries]
    arrays_2.sort(key=lambda x:(int(x[0])))
    entries = [x[1] for x in arrays_2]

    for entry in entries:
        with open('../hotentries/'+ entry,"r") as f:
            line = f.readline()
            words = line.rstrip().split(' ')
        x = []
        for word in words:
            try:
                vec = model.wv[word]
                x.append(vec)
            except:
                print(word)
        if len(x) > 0:
            x_list.append(x)
        else:
            delete_entries.append(entry)
    x_data = [xp.array(x, dtype=xp.float32) for x in x_list]

    x_inp = []
    for x in x_data:
        xi = chainer.functions.dropout(x, ratio=0.5)
        x_inp.append(xi)
    for e in entries:
        if not e in delete_entries:
            with open ('../hotentries/' + e, "r") as f:
                line = f.readline()
            words = line.rstrip().split(' ')
            keys.append(words)

    # teaching
    for key in keys:
        key = ''.join(key)
        try:
            bookmark = masuda[key]
            y_list.append(bookmark)
        except:
            print("no key")
            y_list.append(1)
    y_data = [xp.array([y], dtype=xp.float32) for y in y_list]

    return x_inp, y_data


def output_log(epoch, train_loss, test_loss):
    print("{}, {}, {}".format(epoch, train_loss, test_loss,), flush=True)


def main():
    args = parse_arg()
    x, t = setup_train_data(gpuid=args.gpuid)

    n_input = x[0].shape[1]
    n_output = t[0].shape[0]
    print(n_input,n_output)
    model = SimpleLSTM(n_input, args.n_hidden, n_output, n_layers=args.n_layers, gpuid=args.gpuid)
    if args.resume_from_snapshot:
        chainer.serializers.load_npz(args.resume_from_snapshot+".model", model)
    if 0 <= args.gpuid:
        cuda.get_device_from_id(args.gpuid).use()
        model.to_gpu()

    optimizer = optimizers.Adam()
    optimizer.setup(model)
    if args.resume_from_snapshot:
        chainer.serializers.load_npz(args.resume_from_snapshot+".opt", optimizer)

    data_set = chainer.datasets.TupleDataset(x, t)
    num_data = len(data_set)

    num_train = int(num_data * 0.8)
    train, test = chainer.datasets.split_dataset_random(data_set, num_train)

    train_count = len(train)
    test_count = len(test)

    train_iter = chainer.iterators.SerialIterator(train, args.batch_size)
    test_iter = chainer.iterators.SerialIterator(test, args.batch_size, repeat=False, shuffle=False)

    train_loss = 0
    while train_iter.epoch < args.epoch:
        batch = train_iter.next()
        optimizer.update(model.get_loss_function(), batch)
        train_loss += float(model.loss.array) * len(batch)

        if train_iter.is_new_epoch:
            # evaluation
            test_loss = 0
            with chainer.configuration.using_config('train', False):
                with chainer.using_config('enable_backprop', False):
                    for batch in test_iter:
                        loss_func = model.get_loss_function()
                        loss_func(batch)
                        test_loss += float(model.loss.array) * len(batch)
            test_iter.reset()

            train_loss /= train_count
            test_loss /= test_count
            output_log(train_iter.epoch, train_loss, test_loss)
            train_loss = 0

        if train_iter.epoch % args.save_interval == 0:
            model_path = '{}/mynet_{}.model'.format(args.output_dir, train_iter.epoch)
            optimizer_path = '{}/mynet_{}.opt'.format(args.output_dir, train_iter.epoch)
            chainer.serializers.save_npz(model_path, model)
            chainer.serializers.save_npz(optimizer_path, optimizer)

    model_path = '{}/mynet_final.model'.format(args.output_dir)
    optimizer_path = '{}/mynet_final.opt'.format(args.output_dir)
    chainer.serializers.save_npz(model_path, model)
    chainer.serializers.save_npz(optimizer_path, optimizer)


if __name__ == '__main__':
    main()
