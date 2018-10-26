# sentimentja
Sentiment Analyzer for Japanese


# environment

Anaconda3-5.2.0

For example, if you wanna run anaconda in docker container, you can write this in your Dockerfile:

```
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc
```

# installation

```
git clone https://github.com/sugiyamath/sentiment_ja
cd sentiment_ja
python setup.py install
```

# example usage

```python
from sentimentja import Analyzer
analyzer = Analyzer()
analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"])
```

result

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

