# 把多个集合结合到一个集合
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# ChainMap 使用这个。可以很方便从多个集合搜索数值。
# 比如 先从第一个搜，如果没找到从第二个集合搜·以此类推
from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
# Outputs 1 (from a)
print(c['y'])
# Outputs 2 (from b)
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))
# 可以看出他总是改变集合链中第一个集合
c['z'] = 10
c['w'] = 20
print(a)
print(b)
# 报错，因为第一个集合a 中没有这个key
# del c['y']
# 可以·
del c['x']

# ChainMap 的一些操作
values = ChainMap()
values['x'] = 1
# 添加一个map
values = values.new_child()
values['x'] = 2
# 添加一个map
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# 删除最后添加的map
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)

# 使用update合并dictionary
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)
print(merged['x'])
print(merged['y'])
print(merged['z'])
# 但是注意这种字典合并，若改变原先的字典 合成的merged并不会改变
a['x'] = 100
# 合并后的不发生改变
print(merged['x'])
# 而ChainMap使用的是原生dictionary，他不会有这种情况
merged = ChainMap(a, b)
# 原生的改变
a['x'] = 100
# 合并后的也发生改变
print(merged['x'])

