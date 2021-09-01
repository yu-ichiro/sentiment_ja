import os
import sys
import warnings
import sentimentja
from os.path import dirname, join
warnings.simplefilter(action='ignore', category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

class Analyzer:
    def __init__(self):
        import sentencepiece as spm
        from sentimentja.src import sentiment
        path = dirname(sentiment.__file__)
        self._maxlen = 281
        self._model = sentiment.load(join(path, "model_2021-09-01-13_02.h5"))
        self._sp = spm.SentencePieceProcessor()
        self._sp.load(join(path, "sp.model"))
        self._emolabels = [
            "happy", "sad", "angry", "disgust", "surprise", "fear"
        ]
        self._sentiment = sentiment

    def __call__(self, sentences):
        return self.analyze(sentences)

    def analyze(self, sentences):
        return self._sentiment.predict(
            sentences,
            self._emolabels,
            self._sp,
            self._model,
            self._maxlen)
