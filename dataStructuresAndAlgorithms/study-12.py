# 向列表元素中映射名字，通过名字取得列表元素

# collections.namedtuple() 提供了解决方法。
# 这是一个工厂方法，返回一个标准python元组类型的子类。在你定义的属性中值传递

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# 可以交换元组和一些常用元组操作方法。
print(len(sub))
addr, joined = sub
print(addr)
print(joined)


# 命名元组使用的主要案例：就是解耦可操作元素的位置的代码
# 因此，如果你从数据库调用返回一个大的元组列表，然后通过进入元素位置来操作他们，
# 如果说你在添加一个新列到你的表中，那么你的代码可能会中断。
# 如果说你首先把返回的元组转换成namedtuple,就不会那样

# 普通元组的使用
def compute_cost(records):
	total = 0.0
	for rec in records:
		total += rec[1] * rec[2]
		return total


# 参考这个代码会经常难以表达，更多的是依赖records的结构。
# 下面给出namedtuple的版本
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		total += s.shares * s.price
		return total


# 当然如果records包含了Stock这样的实例·就不需要定义stock
# 下面一些使用方法
s = Stock('ACME', 100, 123.45)
print(s)
# 注意 namedtuple 与 dictionary 不一样。前者是不可变类，后者可变。
# s.shares = 75 会报错
# 如果硬要变，那么使用_replace() 这个方法会产生一个新的namedtuple实例
a = s._replace(shares=75)
print(s)
print(a)
# 还有种使用方法值得注意。就是利用namedtuple做原型。然后将dictionary 转换成namedtuple
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock


def dict_to_stock(s):
	return stock_prototype._replace(**s)
# 使用演示
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
# 最后说一下。如果定义一个高效的数据结构,在这个结构中你会经常改变多个实例属性
# 那么使用namedtuple不是最好的选择。可以定义一个类使用__slots__代替

