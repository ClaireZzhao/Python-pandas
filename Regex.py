# 正则表达式: 用于爬虫时解析字符串，而不是网址

import re 

# [] 或的关系
a = ''
r = re.findall('[0-9]',a) # (正则表达式，要查找的字符串)
r = re.findall('\d',a)

r = re.findall('[^0-9]',a) # 非数字
r = re.findall('\D',a) # 非数字

r = re.findall('x[^de]z',a) # [d-f]

r = re.findall('\w',a) # 提取中文/英文/下划线/数字（特殊字符除外）
r = re.findall('\W',a) # 提取特殊字符，如$,&,\n,\t等

r = re.findall('\s',a) # 提取空白字符, ' ', '\n', '\t'
r = re.findall('\S',a) # 提取非空白字符

r = re.findall('[a-zA-Z]',a) # 提取的是一个个字母
r = re.findall('[a-zA-Z]{3,5}',a) # 最少三个字符，最多5个字符

# 模糊查询
r = re.findall('excel*', a) # *前面的字符匹配0次或无限次

r = re.findall('excel+',a) # +前面的字符匹配1次或无限次

r = re.findall('excel?',a) # ?前面的字符匹配0次或1次


# 开头^,结尾$
tel = '13811115888'
r = re.findall('^\d{11}$',tel) # 从开始到结束之间只能有11位数字，否则返回[]

# () 表示且的关系
r = re.findall('(abc){2}',a) # 两个abc (abc)(xyz)

# 忽略大小写 re.I
r = fe.findall('fbi',a,re.I)

# .匹配任意字符除了换行字符, re.S 表示.可以匹配任意字符包括\n
r = re.findall('fbi.{1}',a,re.I | re.S)


# re.sub替换字符串
r = re.sub('FBI','BBQ',a) # 把FBI替换成BBQ
r = re.sub('FBI','BBQ',a,1) # 1表示只替换一次，默认为0（替换所有）

def 函数名(形参):
    pass
r = re.sub('FBI',函数名,a,1) # 函数名返回空，则相当于把FBI消除

def 函数名(形参):
    分段获取 = 形参.group()
    if int(分段获取) >= 5:
       return '9'
    else:
       return '0'

r = re.sub('\d',函数名,a)

# re.match
r = re.match('\d',a) # a字符串的第一个字符是否为数字，不是的话返回None,是的话返回一个位置
print(r.group()) # r.group() 指返回结果

r = re.search('\d',a) # 遍历整个字符串，找到符合正则表达式的第一个值
print(r.group()) 

r = re.findall('life(.*)python',a) # .* 表示0个或无数个任意字符,结果返回life 和 python之间的内容

a = '123abc456'
r = re.search('([0-9]*)([a-z]*])([0-9]*)',a)
r.group() # 不指定哪个组的话 则全部显示出来
print(r.group(0)) # 写0和不写是一样的
print(r.group(1)) # 第一组
print(r.group(2)) # 第二组
print(r.group(3)) # 第三组
