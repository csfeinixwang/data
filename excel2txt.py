import pandas as pd

df = pd.read_excel('附件1/景区评论.xlsx', sheetname='Sheet1', header=None)		# 使用pandas模块读取数据
print('开始写入txt文件...')
df.to_csv('附件1/景区评论1.txt', header=None, sep=',', index=False)		# 写入，逗号分隔
print('文件写入成功!')
