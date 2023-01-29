# query
条件 = “姓名 in ['李平平', '王刚']”
print(数据.query(条件))

# 以...开头/结尾， 或包含...字符
条件 = 数据['姓名'].str.startswith('王')
print(数据[条件])

条件 = 数据['地址'].str.contains('信阳市')
print(数据[条件])

条件 = 数据['地址'].str.contains('[a-cA-C]座')
print(数据[条件])

# 获取某个时期之前或之后的数据
数据 = pd.read_excel(path, index_col = '出生日期', parse_datess = ['出生日期']
数据2 = 数据.sort_values('出生日期')
数据2.truncate(before='1980').head()
数据2.truncate(after='1990-12').head()
数据2['1983-01-01':'1990-12-01']

数据 = pd.read_excel(path, index_col = '序号', parse_datess = ['出生日期']
条件 = (
		'@数据.出生日期.dt.year > 1980 and'
		'@数据.出生日期.dt.year < 1990'
		'and 性别 == "男"'
)
数据.query(条件)
