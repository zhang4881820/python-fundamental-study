# 通过一个共同key 对 列表进行排序
rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter()这个也可以传入多个参数
# 先根据第一个key排序，在相同情况下，根据第二个key排序
rows_by_lfname = sorted(rows, key=itemgetter('lname','uid'))
print(rows_by_lfname)
# 相当于lamba表达式
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['uid']))
print(rows_by_lfname)
# 那么取最小最大也可以用itemgetter替换
min_rows = min(rows, key=itemgetter('uid'))
max_rows = max(rows, key=itemgetter('uid'))
print('uid最小的item:'+min_rows.__str__())
print('uid最大的item:'+max_rows.__str__())