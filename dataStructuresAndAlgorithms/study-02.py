# 找最大数和最小数

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 如果要找连续的几个最大和最小用heapq的nlargest和nsmallest方法
# 如果只是要找出最小和最大的一个项 那么更快的是直接用min()和max()方法
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(min(nums))

#数组转换成列表
heap = list(nums)
print(heap)
# 列表转换成栈.这个栈的特点是：heap[0] 永远是最小的一项
heapq.heapify(heap)
print(heap)
# 使用 heapq.heappop 可以方便的找出最小数。
# 他是弹出第一个数，然后后面的数列中最小的放置新数列的第一项
print(heapq.heappop(heap))
print(heap)
portfolio = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1},
	{'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09},
	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35},
	{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)


# 实现优先队列
class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]

	@property
	def queue(self):
		return self._queue


# 使用上面定义的类
class Item:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('spam'), 1)
print(q.queue)
print(q.pop())

