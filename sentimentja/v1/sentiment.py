
import tensorflow.compat.v1 as tf
import tensorflow.compat.v1.keras as keras
from tensorflow.compat.v1.keras.preprocessing.sequence import pad_sequences
from tensorflow.compat.v1.keras.models import load_model
import pickle

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
