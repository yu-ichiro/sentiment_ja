import os
import sys
import warnings
import sentimentja
from os.path import dirname, join
warnings.simplefilter(action='ignore', category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

class Analyzer:
    def __init__(self, version=2):
        self._version = version
        if version == 1:
            import tensorflow.compat.v1 as tf
            tf.disable_v2_behavior()
            from sentimentja.v1 import sentiment
            import pickle

            path = dirname(sentiment.__file__)
            
            self._maxlen = 280
            self._model, self._graph = sentiment.load(join(path, "model_2018-08-28-15:00.h5"))

            with open(join(path, "tokenizer_cnn_ja.pkl"), "rb") as f:
                self._tokenizer = pickle.load(f)

            self._emolabels = ["happy", "sad", "disgust", "angry", "fear", "surprise"]
            self._sentiment = sentiment
        elif version == 2:
            import tensorflow.compat.v2 as tf
            tf.enable_v2_behavior()
            import sentencepiece as spm
            from sentimentja.v2 import sentiment

            path = dirname(sentiment.__file__)
            
            self._maxlen = 300
            self._model = sentiment.load(join(path, "model_2019-12-06-15:09.h5"))

            self._sp = spm.SentencePieceProcessor()
            self._sp.load(join(path, "sp.model"))

            self._emolabels = [
                "happy", "sad", "angry", "disgust", "surprise", "fear"
            ]

            self._sentiment = sentiment

    def __call__(self, sentences):
        return self.analyze(sentences)

    def analyze(self, sentences):
        if self._version == 1:
            return self._sentiment.predict(
                sentences,
                self._graph,
                self._emolabels,
                self._tokenizer,
                self._model,
                self._maxlen
            )
        elif self._version == 2:
            return self._sentiment.predict(
                sentences,
                self._emolabels,
                self._sp,
                self._model,
                self._maxlen)
