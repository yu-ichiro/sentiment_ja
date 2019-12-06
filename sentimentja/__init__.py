import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from sentimentja import sentiment


class Analyzer:
    def __init__(self):
        from os.path import dirname, join
        import sentimentja
        import sentencepiece as spm

        path = dirname(sentimentja.__file__)

        self.maxlen = 300
        self.model = sentiment.load(join(path, "model_2019-12-06-15:09.h5"))

        self.sp = spm.SentencePieceProcessor()
        self.sp.load(join(path, "sp.model"))

        self.emolabels = [
            "happy", "sad", "angry", "disgust", "surprise", "fear"
        ]

    def __call__(self, sentences, version=2):
        return self.analyze(sentences)

    def analyze(self, sentences):
        return sentiment.predict(sentences, self.emolabels, self.sp,
                                 self.model, self.maxlen)
