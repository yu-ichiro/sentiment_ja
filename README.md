# sentimentja
Sentiment Analyzer for Japanese Language

# Installation

You can use ```make``` command.

```
git clone https://github.com/sugiyamath/sentiment_ja
cd sentiment_ja
make
```

It will do three phases:

1. Create virtualenv.
2. Install sentiment_ja.
3. Test it.

or just simply this:

```
git clone https://github.com/sugiyamath/sentiment_ja
cd sentiment_ja
python setup.py install
```

# Example usage

First, you need to run ipython.

```
CUDA_VISIBLE_DEVICES=-1 ipython
```

and then, run this code on ipython:

```python
from sentimentja import Analyzer
analyzer = Analyzer()
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
