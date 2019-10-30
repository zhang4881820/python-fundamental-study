# 巧用slice 用来截取集合的

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
# 取2到4位·末尾不取
c = items[2:4]
c = items[a]
print(c)
# 替换
items[a] = [10, 11]
print(items)
# 删除
del items[a]
print(items)

# 使用slice实例可以用一些功能
a = slice(5, 50, 1)
print(a.start)
print(a.stop)
#步长
print(a.step)
# 使用indices 可以返回一个合适的 开始 结束 步长
s = 'HelloWorld'
print(*a.indices(len(s)))
for i in range(*a.indices(len(s))):
	print(s[i])
