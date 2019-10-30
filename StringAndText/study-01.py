# 在多个定界符中的任何一个上分割字符串
# 使用split()，可以使用多个特定的分割规则
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
lineNew = re.split(r'[;,\s]\s*', line)
print(lineNew)

# 分析下这个正则表达式。 `[;,\s]\s*`  首先中括号表示一个字符匹配规则
# 这里面匹配 ; , \s(这个就是空格换行等等的意思)第二个字符是\s*表示后面可以有0-无数个空格或者回车
# 按照这个规则分割完后返回一个数组

# 还有个捕获组的概念。就是在圆括号内。
# 正则表达式（）表示一个子表达式··
# 这个意思就是·：圆括号里的规则捕获到的匹配元素,会被包含在结果当中。
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# 那么如果需要分割，可以这么做
# :: 这个前面的数字就是fields开始位置0开始包含起始位置，后面的数字结尾位置，不包含结尾位置
# 这个意思就是截取0-2位置的，也就是0和1位置的
values = fields[::2]
# 这个表达式意思是·截取1-2位置的数，包含1位置，不包含2位置，然后在末尾加上个''字符
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
# 把前后两个字符串连接起来
values = ''.join(v+d for v, d in zip(values, delimiters))
print(values)
# 不想使用正则的分组，可以这么干（?:）这就是不捕获分组
print(re.split(r'(?:,|;|\s)\s*', line))

