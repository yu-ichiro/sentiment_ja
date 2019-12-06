from setuptools import setup, find_packages

setup(name="sentimentja",
      version="0.0.2a0",
      description="Sentiment Analysis for Japanese",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/sentiment_ja",
      packages=find_packages(),
      install_requires=[
          "tensorflow==2.0.0a0",
          "sentencepiece==0.1.83"
      ],
      package_data={
          'sentimentja':["*"]
      }
)
