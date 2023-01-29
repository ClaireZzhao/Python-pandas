# 数据删除
数据.drop(2) # 删除单行
数据.drop(labels=[1,3]) # 删除多行
数据.drop(labels=['语文', '英语'], axis=1) # 删除多列


# 缺失值处理
data.dropna(subset=['국어', '수학'])
data.fillna({'국어': 0.1, '수학':0.2, '영어':0.3})

data.fillna(method='backfill')
# ffill 用前面的值填充
# bfill 用后面的值填充
# pad      向后填充
# backfill 向前填充


# 去重 & 提重
dataframe.drop_duplicates(subset=['姓名'], keep='first/last'/false)

重复 = data.duplicated(subset='姓名')
data[重复]
