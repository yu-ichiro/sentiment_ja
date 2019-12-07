# sentimentja
Sentiment Analyzer for Japanese Language

If you want to use stable version, see 0.0.1 tag: https://github.com/sugiyamath/sentiment_ja/tree/0.0.1

## Installation

You can use ```make``` command.

```
git clone https://github.com/sugiyamath/sentiment_ja
cd sentiment_ja
make
```

or just simply this:

```
git clone https://github.com/sugiyamath/sentiment_ja
cd sentiment_ja
python setup.py install
```

## Example usage

First, you need to run ipython.

```
CUDA_VISIBLE_DEVICES=-1 ipython
```

and then, run this code on ipython:

```python
from sentimentja import Analyzer
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

analyzer = Analyzer(version=1)
analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"])
```

[result]

```python
[
  {
    'sentence': 'ファイナル・ファンタジーは楽しい',
    'emotions': {'happy': '32.0', 'sad': '2.0', 'disgust': '2.0', 'angry': '1.0', 'fear': '1.0', 'surprise': '4.0'}
  },
  {
    'sentence': 'クソゲーはつまらん',
    'emotions': {'happy': '1.0', 'sad': '2.0', 'disgust': '22.0', 'angry': '5.0', 'fear': '5.0', 'surprise': '1.0'}
  }
]
```

or if you want to use version=2, this:

```python
from sentimentja import Analyzer
import tensorflow.compat.v2 as tf
tf.enable_v2_behavior()

analyzer = Analyzer(version=2)
analyzer(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"])
```

Note: Currently, this project supports tensorflow==2.0.0a0 only.

Note: If you specify ```Analyzer(version=2)```, the output is more accurate than version 1.