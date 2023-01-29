data2 = pd.pivot_table(data, index=['部门', '人员'], values=['数量', '金额'], columns='所属区域', aggfunc=[sum, np.mean])

data3 = pd.crosstab([data.日期.dt.month, data.所属区域], data.部门, margins=True)
