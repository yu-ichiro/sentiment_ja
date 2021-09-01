# sentimentja
Sentiment Analyzer for Japanese Language

- stable version: https://github.com/sugiyamath/sentiment_ja/tree/0.0.1
- train your own model: https://github.com/sugiyamath/sentiment_ja_train

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

Run ipython.

```
CUDA_VISIBLE_DEVICES=-1 ipython
```

and then, run this code:

```python
from sentimentja import Analyzer
from pprint import pprint

analyzer = Analyzer()
pprint(analyzer.analyze([
    "final fantasy 14 超楽しい",
    "クソゲーはつまらん",
    "エアリスが死んで悲しい",
    "冒険の書が消える音こわい",
    "廃人ゲーマーのスキルすごい",
    "ケフカキモい"
]))
```

[result]

```python
[{'emotions': {'angry': 0.38450825,
               'disgust': 0.34049153,
               'fear': 0.21595812,
               'happy': 0.9386289,
               'sad': 0.34736797,
               'surprise': 0.4474829},
  'sentence': 'final fantasy 14 超楽しい'},
 {'emotions': {'angry': 0.849911,
               'disgust': 0.84053206,
               'fear': 0.35027078,
               'happy': 0.26533514,
               'sad': 0.3436579,
               'surprise': 0.2612424},
  'sentence': 'クソゲーはつまらん'},
 {'emotions': {'angry': 0.3113451,
               'disgust': 0.51893616,
               'fear': 0.64312303,
               'happy': 0.049518317,
               'sad': 0.89467585,
               'surprise': 0.5028756},
  'sentence': 'エアリスが死んで悲しい'},
 {'emotions': {'angry': 0.38816807,
               'disgust': 0.27659303,
               'fear': 0.90935254,
               'happy': 0.07564357,
               'sad': 0.5684624,
               'surprise': 0.51281214},
  'sentence': '冒険の書が消える音こわい'},
 {'emotions': {'angry': 0.3801153,
               'disgust': 0.62795836,
               'fear': 0.5906316,
               'happy': 0.19693395,
               'sad': 0.17561686,
               'surprise': 0.89091665},
  'sentence': '廃人ゲーマーのスキルすごい'},
 {'emotions': {'angry': 0.6396977,
               'disgust': 0.90158427,
               'fear': 0.64611995,
               'happy': 0.18225843,
               'sad': 0.3184908,
               'surprise': 0.37674865},
  'sentence': 'ケフカキモい'}]
```
