result = pd.merge(data1, data2.loc[:, ['学号', '总分']], how='left', on='学号')
结果_总分 = result.总分
结果 = 结果.drop('总分', axis=1)
结果.insert(0, '总分', 结果_总分）   # 把总分列放在最前面

# 在原表上修改
writer = pd.ExcelWriter(路径)
结果.to_excel(writer, index=False)
writer.save()
writer.close()
