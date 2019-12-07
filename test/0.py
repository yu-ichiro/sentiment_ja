from sentimentja import Analyzer
from pprint import pprint
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

analyzer = Analyzer(version=1)
pprint(analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"]))
