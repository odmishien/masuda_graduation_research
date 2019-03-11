import six

import numpy
import chainer
import chainer.links as L
import chainer.functions as F
from chainer.backends import cuda


class SimpleLSTM(chainer.Chain):
    def __init__(self, n_input, n_hidden, n_output, n_layers=1, dropout_rate=0.5, gpuid=-1):
        super(SimpleLSTM, self).__init__()
        with self.init_scope():
            self.lstm = L.NStepLSTM(n_layers=n_layers, in_size=n_input, out_size=n_hidden, dropout=dropout_rate)
            self.lin = L.Linear(in_size=n_hidden, out_size=n_output)
        self.gpuid = gpuid

    def forward(self, x):
        _, _, out = self.lstm(hx=None, cx=None, xs=x)
        y_list = []
        for o in out:
            y = self.lin(o)
            y_list.append(y[-1])
        return y_list

    def get_loss_function(self):
        def lf(dat):
            x = [d[0] for d in dat]
            t = [d[1] for d in dat]

            y = self.forward(x)

            loss = 0
            for b in six.moves.range(len(y)):
                loss += F.mean_squared_error(y[b], t[b])
            self.loss = loss
            return self.loss
        return lf
