#-*- coding: utf-8 -*-
class Config:
    #-------------------------------------
    #  クラス数
    #-------------------------------------
    NUM_CLASSES = 1

    #-------------------------------------
    #  入力画像の大きさ
    #-------------------------------------
    # 1単語のベクトルサイズ
    WORD_VEC_SIZE = 100
    # １文の最大単語数
    MAX_WORDS_IN_TXT = 100
    # モノクロ？

    #-------------------------------------
    #  畳み込み層の情報
    #-------------------------------------
    # フィルタの大きさ
    CONV_SIZE = 16
    # 第1層目のマップ数
    CONV1_OUT_CHANNELS = 32
    # 第2層目のマップ数
    CONV2_OUT_CHANNELS = 64

    #-------------------------------------
    #  全結合層の情報
    #-------------------------------------
    # 第１層目のニューロン数
    # CONV_SIZEによって決まる
    # 間違って入れば実行時に Chainer が教えてくれる
    NUM_HIDDEN_NEURONS1 = 20736
    # 第２層目のニューロン数
    NUM_HIDDEN_NEURONS2 = 1024

    #-------------------------------------
    #  学習時のバッチサイズ
    #-------------------------------------
    BATCH_SIZE = 100
