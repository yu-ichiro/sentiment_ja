from sentimentja import Analyzer
from pprint import pprint

analyzer = Analyzer(version=2)
pprint(analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"]))
