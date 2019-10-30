# 使用shell通配符模式匹配字符串
# 在使用unix shell 情况下
# fnmatch 模块 provides two functions—fnmatch() and fnmatchcase()

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# fnmatchcase 是严格区分大小写的，fnmatch在window中不区分·在OS（mac）中区分。
print(fnmatchcase('foo.txt', '*.TXT'))
print(fnmatch('foo.txt', '*.TXT'))

addresses = ['5412 N CLARK ST',
             '1060 W ADDISON ST',
             '1039 W GRANVILLE AVE',
             '2122 N CLARK ST',
             '4802 N BROADWAY',
             ]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# 最后提一下使用glob 模块替代fnmatch 更好。