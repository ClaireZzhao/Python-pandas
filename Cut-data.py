import pandas as pd
年份 = [1992, 1983, 1922, 1932, 1973]
箱子 = [1900, 1950, 2000]
箱子名称 = ['50年代前', '50年代后']
结果 = pd.cut(年份, 箱子, labels=箱子名称)
print(pd.value_counts(结果))

# 等宽分箱
import pandas as pd
年份 = [1992, 1983, 1922, 1932, 1973, 1999, 1993, 1995]
结果 = pd.qcut(年份, q=4)
print（pd.value_counts(结果))
