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
