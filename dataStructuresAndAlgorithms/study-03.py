# 集合字典类 map list set
# 字典类的结构就是键值对形式一对一。
# 如果你要一个key对应多个value 那么使用 list 或者 set
# 如果想使用有序的数列那么用list
# 如果要使用没有重复的数列那么用set
# 一个简单的集合结构。defaultdict.特点是自动初始化第一个值，以便可以简单的做些add操作

from collections import defaultdict
# 构建默认list 可以排序
dlist = defaultdict(list)
dlist['a'].append(8)
dlist['a'].append(2)
dlist['b'].append(4)
dlist['a'].append(2)
dlist['a'].sort()
print(dlist)
# 没有重复值
dset = defaultdict(set)
dset['a'].add(8)
dset['a'].add(2)
dset['a'].add(2)
dset['b'].add(4)
print(dset)

# 控制集合中每项的顺序可以用集合模块中的OrderedDict
# OrderedDict 两倍list列表，key的顺序按照插入顺序，已经存在的key不改变顺序
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# 输出顺序
for key in d:
	print(key, d[key])

import json
# 转换成json格式
print(json.dumps(d))
