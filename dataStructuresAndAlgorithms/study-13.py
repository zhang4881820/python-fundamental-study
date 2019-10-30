# 同时改变和减少数据
# 使用 generator-expression 参数 。 也就是循环迭代
nums = [1, 2, 3, 4, 5]
# 一边遍历减少nums中的数据·一边做计算。
s = sum(x * x for x in nums)
print(s)
# 其他例子
import os

files = os.listdir('/pythonStudy')
if any(name.endswith('.py') for name in files):
	print('There be python!')
else:
	print('Sorry, no python.')
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [{'name': 'GOOG', 'shares': 50},
             {'name': 'YHOO', 'shares': 75},
             {'name': 'AOL', 'shares': 20},
             {'name': 'SCOX', 'shares': 65}
             ]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
a = min(portfolio, key=lambda s : s['shares'])
print(a)
