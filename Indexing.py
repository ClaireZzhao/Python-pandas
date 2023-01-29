# 设置分层索引
data = pd.read_excel(path, sheet_name = '1', index_col = [0, 1])
data = data.set_index(['班级', '学号'])

# 多层索引查询
data2 = data.loc[('1班', slice(None))]
data2 = data.loc[(('1班', 'a'), slice(None))]

# 遇到无序的数据时先排序再查询
data = data.sort_index(level = '科目')
data2= data.loc[('语文', slice(None))]

# 设置多层行索引
index = pd.MultiIndex.from_product([[2019, 2020], [5, 6]], names=['年', '月'])
# 设置多层列索引
columns = pd.MultiIndex.from_product([['香蕉', '苹果'], ['土豆', '茄子']], names=['水果', '蔬菜'])
data = pd.DataFrame(np.random.random(size(4, 4)), index = index, columns=columns)

# 多层索引运算
data = pd.read_excel(path, header=[0,1])
总计 = 数据['土豆'] + 数据['倭瓜']
总计.columns = pd.MultiIndex.from_product([['总计'], 总计.columns])
结果 = pd.concat([数据, 总计], axis=1) # 横向粘贴
print(结果)
