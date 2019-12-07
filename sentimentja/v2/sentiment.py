import tensorflow as tf


def preprocess(data, sp, maxlen=300):
    return tf.keras.preprocessing.sequence.pad_sequences(
        [sp.EncodeAsIds(text) for text in data],
        maxlen=maxlen)


def predict(sentences, emolabels, sp, model, maxlen):
    preds = []
    targets = preprocess(sentences, sp, maxlen=maxlen)
    for i, ds in enumerate(model.predict(targets)):
        preds.append({
            "sentence":
            sentences[i],
            "emotions":
            dict(zip(emolabels, [str(round(100.0 * d)) for d in ds]))
        })
    return preds


def load(path):
    model = tf.keras.models.load_model(path)
    return model
