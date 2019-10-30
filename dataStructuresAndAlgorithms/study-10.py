# 过滤列表元素

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
a = [n for n in mylist if n > 0]
print(a)
b = [n for n in mylist if n < 0]
print(b)

# 另一种方式
# 如果mylist很大 可能会产生很大的结果
# 可以使用generator 表达式 去生成已经过滤的可迭代的值
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
	print(x)

# 有时候过滤的标准在列表含义和generator表达式种不那么容易表达
# 例如一个涉及到异常处理的过滤处理或者其他一些复杂的细节
# 因此，可以把过滤代码封装在函数中，然后用filter()构建。例子如下
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
	try:
		# 将值转换成整型
		x = int(val)
		return True
	# 捕获异常
	except ValueError:
		return False


# filter() 函数会生成一个迭代器（iterator），所以，想要得到一个列表结果·
# 可以用 list() 包裹下
ivals = list(filter(is_int, values))
print(ivals)  # Outputs ['1', '2', '-3', '4', '5']

# 使用过滤器 改变数据值
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math

a = [math.sqrt(n) for n in mylist if n > 0]
print(a)
# 替换不匹配过滤规则的数据
# 如果不满足大于0的条件，那么用0替换
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
# 如果不满足小于0的条件，那么用0替换
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

# 还有一个著名的过滤工具itertools.compress(),
# 可以和一个布尔列表一起迭代·
# 返回布尔列表中对应的true位置的元素
addresses = [
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH',
	'2122 N CLARK',
	'5645 N RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BROADWAY',
	'1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
# compress() 也是返回一个迭代器 所以可以用list 把结果转成列表
a = list(compress(addresses, more5))
print(a)
