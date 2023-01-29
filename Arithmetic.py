result = data['a'].fillna(0) + data['b'].fillna(0)
result = data['a'].add(data['b'], fill_value = 0)

'''
方法  反转方法  描述
add.  radd.  加法
sub   rsub   减法
div   rdiv   除法
floordiv rfloorfiv 整除
mul   rmul   乘法
'''

# 把inf替换成NaN
pd.options.mode.use_inf_as_na = True
