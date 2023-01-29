path = ''
data = pd.read_excel(path)
data2 = data.groupby(['城市','区'])[['人数', '金额']].sum()
print(data2)

path = ''
data = pd.read_excel(path)
字典 = {'1月':'count', '2月':sum, '3月':max, '4月':'mean'}
data2 = data.groupby('店号').agg(字典)  # agg函数一般与groupby配合使用
# agg是基于列的聚合操作，而groupby是基于行的

path = ''
data = pd.read_excel(path, index_col='店号')
对应关系 = {'1月':'一季度', '2月':'一季度', '3月':'一季度', '4月':'二季度'}
data2 = data.groupby(对应关系, axis=1)
print(data2.sum())

# 按字符长度进行聚合计算
path = ''
data = pd.read_excel(path, index_col='城市')
data2 = data.groupby(len).sum()
print(data2)

path = ''
data = pd.read_excel(path, index_col=[0,1])  # ['班级','性别']
data3 = data.groupby(level='班级').mean()
print(data3)

path = ''
data = pd.read_excel(path, header=[0,1])
L1 = ['一季度','一季度','一季度','二季度','二季度']
L2 = ['1月','2月','3月','4月','5月']
多层索引 = pd.MultiIndex.from_arrays([L1, L2], names=['季度','月份'])
data2 = pd.DataFrame(data,columns=多层索引)
data3 = data2.groupby(level='季度', axis=1).sum()
print(data3)
