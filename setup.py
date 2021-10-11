from setuptools import setup, find_packages

setup(name="sentimentja",
      version="0.0.3b",
      description="Sentiment Analysis for Japanese",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/sentiment_ja",
      packages=['sentimentja', 'sentimentja.src'],
      install_requires=[
          "tensorflow>=2.7.0",
          "sentencepiece==0.1.96"
      ],
      package_data={
          'sentimentja':["*"],
          'sentimentja.src':["*"],
      }
)
