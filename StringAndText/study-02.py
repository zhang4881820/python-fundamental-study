# 以一个字符串的开始或结束匹配文本
# 主要两个方法str.starts with() or str.endswith()
filename = 'spam.txt'
start = filename.startswith('file:')
end = filename.endswith('.txt')
print(start)
print(end)

import os

# 列出当前文件所在目录下的所有文件
filenames = os.listdir('.')
print(filenames)
name = [name for name in filenames if name.endswith(('.py', '01.py'))]
print(name)
# 判斷有沒有.py结尾的文件名字
a = any(name.endswith('.py') for name in filenames)
print(a)
# 其他例子
from urllib.request import urlopen


def read_data(name):
	if name.startswith(('http:', 'https:', 'ftp:')):
		return urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()


# 使用
choices = ['http:', 'ftp:']
url = 'http://www.baidu.com'
# 会报错，因为需要字符串或者元组参数 而不是list
# url.startswith(choices)
url.startswith(tuple(choices))
# result = read_data(url)
# print(result)

# 一些其他使用技巧
# 判断后四位是不是和.txt相等
filename = 'spam.txt'
print(filename[-4:] == '.txt')
# 判断前几位是否与对应字符串匹配
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

# 继续使用正则来玩玩
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
