from sentimentja import sentiment

class Analyzer:
    def __init__(self):
        import sentimentja
        import pickle
        from keras.preprocessing.sequence import pad_sequences
        from keras.models import load_model
        from os.path import dirname, join

        path = dirname(sentimentja.__file__)
        
        self.maxlen = 280
        self.model, self.graph = sentiment.load(join(path, "model_2018-08-28-15:00.h5"))

        with open(join(path, "tokenizer_cnn_ja.pkl"), "rb") as f:
            self.tokenizer = pickle.load(f)

        self.emolabels = ["happy", "sad", "disgust", "angry", "fear", "surprise"]

    def analyze(self, sentences):
        return sentiment.predict(
            sentences,
            self.graph,
            self.emolabels,
            self.tokenizer,
            self.model,
            self.maxlen
        )
