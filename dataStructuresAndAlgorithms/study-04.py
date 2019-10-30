# 集合字典类的计算
prices = {
	'ACME': 45.23,
	'AAPL': 612.23,
	'IBM': 205.23,
	'HPQ': 37.23,
	'FB': 10.23,
}
# 求大小用zip倒置key values
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
# 排序
sortPrices = sorted(zip(prices.values(), prices.keys()))
print(sortPrices)
# zip()方法会自动创建一个迭代器·但是只能使用一次
prices_and_name = zip(prices.values(), prices.keys())
print(min(prices_and_name))
# 下面使用就会报错了
# print(max(prices_and_name))

# 找两个集合中共有的部分或者相异的部分
a = {
	'x': 1,
	'y': 2,
	'z': 3,
}
b = {
	'w': 10,
	'x': 11,
	'y': 2,
}
# 找共有的key
c = a.keys() & b.keys()
print(c)
# 找在a中有，在b中没有的key
c = a.keys() - b.keys()
print(c)
# 找共有的key-value 对
c = a.items() & b.items()
print(c)
# 选中的key并去除得到一个新集合
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)


# 在集合中保证集合顺序的情况下去除重复元素
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			# 就是让item具备迭代作业
			yield item
			seen.add(item)


def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			# 就是让item具备迭代作业
			yield item
			seen.add(val)


a = [1, 5, 5, 2, 3, 4, 5, 6, 7, 8, 4, 1]
print(list(dedupe(a)))
a = [{'x': 1, 'y': 2},
     {'x': 1, 'y': 3},
     {'x': 1, 'y': 2},
     {'x': 2, 'y': 4},
     ]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))