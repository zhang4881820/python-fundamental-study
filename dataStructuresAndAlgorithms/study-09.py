# 基于某个属性进行分组记录
rows = [{'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]

from operator import itemgetter
from itertools import groupby

# 根据日期属性排序.强调一下必须先根据你要分组的属性排好序。不然就没办法分组
rows.sort(key=itemgetter('date'))
# 分组迭代
for date, items in groupby(rows, key=itemgetter('date')):
	print(date)
	for i in items:
		print(' ', i)

# 另一种分组方法
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
	rows_by_date[row['date']].append(row)
print(rows_by_date)

for r in rows_by_date['07/01/2012']:
	print(r)
