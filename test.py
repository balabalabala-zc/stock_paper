# -*- coding:utf-8 -*-

import re
import os
import requests
import sys
import glob

reload(sys)
sys.setdefaultencoding('utf8')


def my_replace(match):
    print(match.group())
    return "a"

if __name__ == '__main__':
    names = ['', u'教你炒股票1：不会赢钱的经济人，只是废人！', u'教你炒股票2：没有庄家，有的只是赢家和输家！', u'教你炒股票3：你的喜好，你的死亡陷阱！(2006-06-09）', u'教你炒股票4：什么是理性？今早买N中工就是理性！', u'教你炒股票5：市场无须分析，只要看和干！', u'教你炒股票6：本ID如何在五粮液、包钢权证上提款的！', u'教你炒股票7：给赚了指数亏了钱的一些忠告', u'教你炒股票8：投资如选面首，G点为中心，拒绝ED男！', u'教你炒股票9：甄别“早泄”男的数学原则！', u'教你炒股票10：2005年6月，本ID为何时隔四年后重看股票', u'教你炒股票11：不会吻，无以高潮！', u'教你炒股票12：一吻何能消魂？', u'教你炒股票13：不带套的操作不是好操作！', u'教你炒股票14：喝茅台的高潮程序！', u'教你炒股票15：没有趋势，没有背驰', u'教你炒股票16：中小资金的高效买卖法', u'教你炒股票17：走势终完美', u'教你炒股票18：不被面首的雏男是不完美的', u'教你炒股票19：学习缠中说禅技术分析理论的关键', u'教你炒股票20：缠中说禅走势中枢级别扩张及第三类买卖点', u'教你炒股票21：缠中说禅买卖点分析的完备性', u'教你炒股票22：将8亿的大米装到5个庄家的肚里', u'教你炒股票23：市场与人生', u'教你炒股票24：MACD对背弛的辅助判断', u'教你炒股票25：吻，MACD、背弛、中枢', u'教你炒股票26：市场风险如何回避', u'教你炒股票27：盘整背驰与历史性底部', u'教你炒股票28：下一目标：摧毁基金', u'教你炒股票29：转折的力度与级别', u'教你炒股票30：缠中说禅理论的绝对性', u'教你炒股票31：资金管理的最稳固基础', u'教你炒股票32：走势的当下与投资者的思维方式', u'教你炒股票33：走势的多义性', u'教你炒股票34：宁当面首，莫成怨男', u'教你炒股票35：给基础差的同学补补课', u'教你炒股票36：走势类型连接结合性的简单运用', u'教你炒股票37：背驰的再分辨', u'教你炒股票38：走势类型连接的同级别分解', u'教你炒股票39：同级别分解再研究', u'教你炒股票40：同级别分解的多重赋格', u'教你炒股票41：没有节奏，只有死', u'教你炒股票42：有些人是不适合参与市场的', u'教你炒股票43：有关背驰的补习课', u'教你炒股票44：小级别背驰引发大级别转折', u'教你炒股票45：持股与持币，两种最基本的操作', u'教你炒股票46：每日走势的分类', u'教你炒股票47：一夜情行情分析', u'教你炒股票48：暴跌，牛市行情的一夜情', u'教你炒股票49：利润率最大的操作模式', u'教你炒股票50：操作中的一些细节问题', u'教你炒股票51：短线股评荐股者的传销把戏', u'教你炒股票52：炒股票就是真正的学佛', u'教你炒股票53：三类买卖点的再分辨',
             u'教你炒股票54：一个具体走势的分析', u'教你炒股票55：买之前戏，卖之高潮', u'教你炒股票56：530印花税当日行情图解', u'教你炒股票57：当下图解分析再示范', u'教你炒股票58：图解分析示范三', u'教你炒股票59：图解分析示范四', u'教你炒股票60：图解分析示范五', u'教你炒股票61：区间套定位标准图解（分析示范六）', u'教你炒股票62：分型、笔与线段', u'教你炒股票63：替各位理理基本概念', u'教你炒股票64：去机场路上给各位补课', u'教你炒股票65：再说说分型、笔、线段', u'教你炒股票66：主力资金的食物链', u'教你炒股票67：线段的划分标准', u'教你炒股票68：走势预测的精确意义', u'教你炒股票69：月线分段与上海大走势分析、预判', u'教你炒股票70：一个教科书式走势的示范分析', u'教你炒股票71：线段划分标准的再分辨', u'教你炒股票72：本ID已有课程的再梳理', u'教你炒股票73：市场获利机会的绝对分类', u'教你炒股票74：如何躲避政策性风险', u'教你炒股票75：逗庄家玩的一些杂史1', u'教你炒股票76：逗庄家玩的一些杂史2', u'教你炒股票77：一些概念的再分辨', u'教你炒股票78：继续说线段的划分', u'教你炒股票79：分型的辅助操作与一些问题的再解答', u'教你炒股票80：市场没有同情、不信眼泪', u'教你炒股票81：图例、更正及分型、走势类型的哲学本质', u'教你炒股票82：分型结构的心理因素', u'教你炒股票83：笔-线段与线段-最小中枢结构的不同心理意义1', u'教你炒股票84：本ID理论一些必须注意的问题', u'教你炒股票85：逗庄家玩的一些杂史3', u'教你炒股票86：走势分析中必须杜绝一根筋思维', u'教你炒股票87：逗庄家玩的一些杂史4', u'教你炒股票88：图形生长的一个具体案例', u'教你炒股票89：中阴阶段的具体分析', u'教你炒股票90：中阴阶段结束时间的辅助判断', u'教你炒股票91：走势结构的两重表里关系1', u'教你炒股票92：中枢震荡的监视器', u'教你炒股票93：走势结构的两重表里关系2', u'教你炒股票94：当机立断', u'教你炒股票95：修炼自己', u'教你炒股票96：无处不在的赌徒心理', u'教你炒股票97：中医、兵法、诗歌、操作1', u'教你炒股票98：中医、兵法、诗歌、操作2', u'教你炒股票99：走势结构的两重表里关系3', u'教你炒股票100：中医、兵法、诗歌、操作3', u'教你炒股票101：答疑1', u'教你炒股票102：再说走势必完美', u'教你炒股票103：学屠龙术前先学好防狼术', u'教你炒股票104：几何结构与能量动力结构1', u'教你炒股票105：远离聪明、机械操作', u'教你炒股票106：均线、轮动与缠中说禅板块强弱指标', u'教你炒股票107：如何操作短线反弹', u'教你炒股票108：何谓底部？从月线看中期走势演化']

    for i, name in enumerate(names):
        print('<li><a href="%03d.html">%s</a></li>' % (i, name))
    sys.exit(0)

    files = glob.glob("*.html")
    files.sort()

    for file_name in files:
        with open(file_name, 'r') as f:
            buf = f.read(1024 * 1024 * 1024)
            buf1 = re.sub(
                "href=\"http://blog.sina.com.cn[^<]+", my_replace, buf)

        break