# 环比
上月 = 数据.销售金额.shift()   # 销售金额的数据全部往下移一格
环比 = 数据.销售金额 - 上月
数据['环比增长金额'] = 环比

 def function(新数据):
		 新数据['环比'] = 新数据.金额 - 新数据.金额.shift()
		 return 新数据 
数据2 = 数据.sort_values(['城市','月份']).groupby('城市').apply(function)

# 同比
年 = data['日期'].dt.year
数据2 = pd.pivot_table(数据, index='店号', values='金额', columns=年, aggfunc='sum')数据2['同比'] = (数据2[2019]-数据2[2018]) / 数据2[2018]
