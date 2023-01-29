数据['城市2'] = 数据['城市2'].str.replace('城八', '市')
数据.replace('[A-Z]', 88, regex=True, inplace=True) # 正则表达式
data['온도'].str.replace('C', '').astype('int64'))

data['이름'].str.cat(sep=','))
data['이름'].str.cat(['변신']*len(data), sep='^', na_rep='@')

data['상태'].str.split('피', expand=True) # 以指定的字符将对象分成两列或多列

data['상태'].str.partition('blood')

data['상태'].str.get(2)

data['station'].str.slice(0,3,2) # 从0开始到3结束， 隔一个取
data['station'].str.slice_replace(0,3,'520') 

data['station'].str.join('a') # 根据指定的字符进行连接

data['station'].str.contain('blood', na='没有') # 返回布尔值

data['station'].str.startswith('满')
data['station'].str.endswith('满')

data['name'].str.repeat(3) # 字符串重复3次

data['station'].str.pad(5, fillchar='&', side='right')  
# 指定字符长度为5个字符，长度不够用&填充, 默认从左边补齐 (side='right'/'both')

data['station'].str.zfill(10) # 用0填充至10个字符

data['station'].str.encode('utf-8')

data['station'].str.strip('中远近离'） # 将括号内的字符从两边去除
# lstrip 从左边去除
 # rstrip  从右边去除

data['里程'].str.get_dummies('距') # 以括号内的内容对字符串做分割 

字典 = str.maketrans({'距':'ju', '离':'li'})
data['里程'].str.translate(字典))

数据['日期'].astype('str').str.find('-') #找出括号内的内容出现的第一个位置的index，没有的话返回-1

data.str.lower()
data.str.upper()
data.str.title() # 每一个单词的首字母大写
data.str.capitalize() # 第一个字母大写
data.str.swapcase()  # 大小写交换

data['状态'].str.match('.{2}激') # 利用正则表达式
data['日期'].astype('str').str.extract('(\d{4})-(\d{2})-(\d{2})') # 只展示括号内的内容

# 将中文日期格式转换为英文日期格式
data['日期'].astype('str').str.replace('(\d+)-(\d+)-(\d+)', r'\3/\2/\1')
