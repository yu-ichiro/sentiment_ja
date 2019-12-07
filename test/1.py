from sentimentja import Analyzer
from pprint import pprint
import tensorflow.compat.v2 as tf
tf.enable_v2_behavior()

analyzer = Analyzer(version=2)
pprint(analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"]))
