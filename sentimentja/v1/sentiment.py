
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
import tensorflow as tf

def preprocess(data, tokenizer, maxlen=280):
    return(pad_sequences(tokenizer.texts_to_sequences(data), maxlen=maxlen))

def predict(sentences, graph, emolabels, tokenizer, model, maxlen):
    preds = []
    targets = preprocess(sentences, tokenizer, maxlen=maxlen)
    with graph.as_default():
        for i, ds in enumerate(model.predict(targets)):
            preds.append({
                "sentence":sentences[i],
                "emotions":dict(zip(emolabels, [str(round(100.0*d)) for d in ds]))
            })
    return preds

def load(path):
    model = load_model(path)
    graph = tf.get_default_graph()
    return model, graph

if __name__ == "__main__":
    maxlen = 280
    model, graph = load("models/model_2018-08-28-15:00.h5")

    with open("models/tokenizer_cnn_ja.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    emolabels = ["happy", "sad", "disgust", "angry", "fear", "surprise"]
        
    examples = [
        "まじきもい、あいつ",
        "今日は楽しい一日だったよ",
        "ペットが死んだ、実に悲しい",
        "ふざけるな、死ね",
        "ストーカー怖い",
        "すごい！ほんとに！？",
        "葉は植物の構成要素です。",
        "ホームレスと囚人を集めて革命を起こしたい"
    ]

    print(predict(examples, graph, emolabels, tokenizer, model, maxlen))
