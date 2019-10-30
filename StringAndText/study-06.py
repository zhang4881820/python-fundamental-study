# 大小写问题
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
# 忽视大小写
print(re.findall('python', text, flags=re.IGNORECASE))
# 忽视大小写 替换
new_line = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(new_line)

# 但是替换文本有个限制就是大小写匹配替换。
# 意思就是找到的匹配项是大写的·那么用大写的替换，so
# 要实现他·需要定义一个回调函数支持·如下
def matchcase(word):
	def replace(m):
		text = m.group()
		if text.isupper():
			return word.upper()
		elif text.islower():
			return word.lower()
		elif text[0].isupper():
			return word.capitalize()
		else:
			return word
	return replace

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

# re.IGNORECASE 提一下·这对于unicode的大小写匹配支持不足够