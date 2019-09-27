from sentimentja import Analyzer
from pprint import pprint

analyzer = Analyzer()
pprint(analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"]))
