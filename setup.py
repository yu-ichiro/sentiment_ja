from setuptools import setup, find_packages

setup(name="sentimentja",
      version="0.0.1b",
      description="Sentiment Analysis for Japanese",
      author="Shun Sugiyama",
      url="https://github.com/sugiyamath/sentiment_ja",
      packages=find_packages(),
      install_requires=[
          "keras==2.0.8",
          "tensorflow==1.9.0"
      ],
      package_data={
          'sentimentja':["*"]
      }
)
