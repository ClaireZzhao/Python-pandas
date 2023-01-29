字典 = {'男':'先生', '女':'女士'}
data['称呼'] = data['性别'].map(字典)

# 当函数里有一个参数时
def 替换(x):
		称呼 = '先生' if x=='男' else '女士'
		return 称呼
data['称呼'] = data['性别'].map(替换)

# 当函数里有多个参数时用apply， apply 还可以用于表操作
def 修改分数(x, 误差值):
		return x+误差值
data['语文'] = data['语文'].apply(修改分数, args=(-3,)) # args 用于传参数

# 行计算
data2 = data[['语文', '数学', '英语']].apply(sum, axis=0)    # 行总计

# 列计算
def bmi(数据):
		身高 = 数据['身高']
    体重 = 数据['体重']
		bmi = 体重 / （身高**2）
		return bmi

data['bmi'] = data.apply(bmi, axis=1)

# applymap
data2 = data.applymap(lambda x:'%.3f' % x)
