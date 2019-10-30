# 在字符串中脱离不想要的字符 例如空白格

# strip()，lstrip() and rstrip() 这几个方法默认去除空格和回车·。
# 第一个前后，第二个左 ，第三个 右

s = '   hello world   \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
# 但是没办法处理内部的空格！
s = ' hello world \n'
s = s.strip()
# 中间的空格没办法处理
print(s)
# 这个时候可以用replace()方法来做
print(s.replace(' ', ''))
# 或者正则substitution
import re

print(re.sub(r'\s+', '', s))

# generator expression 来做 就是迭代· 读一行写一行
# 这是非常高效的··
with open('study-01.py', 'r', encoding='utf-8') as f:
	lines = (line.strip() for line in f)
	for line in lines:
		print(line)