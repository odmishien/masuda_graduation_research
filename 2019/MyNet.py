from chainer import Chain
import chainer.links as L
import chainer.functions as F

from config import Config as C


class MySubNet(Chain):
    def __init__(self, in_ch, ch1, cv1, ch2, cv2):
        super().__init__()
        with self.init_scope():
            self.conv1 = L.Convolution2D(in_ch, ch1, cv1)
            self.conv2 = L.Convolution2D(ch1, ch2, cv2)

    def forward(self, x):
        h_1 = F.relu(self.conv1(x))
        h_2 = self.conv2(h_1)
        h_3 = F.max_pooling_2d(h_2, ksize=(4, 4))
        h_4 = F.local_response_normalization(h_3)
        return F.relu(h_4)


class MyNet(Chain):
    def __init__(self):
        super().__init__()
        with self.init_scope():
            self.subNet = MySubNet(1, C.CONV1_OUT_CHANNELS, C.CONV_SIZE, C.CONV2_OUT_CHANNELS, C.CONV_SIZE)
            self.fullLayer1 = L.Linear(C.NUM_HIDDEN_NEURONS1, C.NUM_HIDDEN_NEURONS2)
            self.fullLayer2 = L.Linear(C.NUM_HIDDEN_NEURONS2, C.NUM_CLASSES)

#    def train(self, x, y_hat):
#        y = self.forward(x)
#        return F.mean_squared_error(y, y_hat)

    def __call__(self, x, y_hat = None):
        h = self.subNet.forward(x)
        h = F.dropout(F.relu(self.fullLayer1(h)))
        y = self.fullLayer2(h)
        if y_hat is None:
            return y
        else:
            return F.mean_squared_error(y, y_hat)
