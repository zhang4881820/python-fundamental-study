# 指定最短匹配的正则表达式
import re

# 模板\"(.*)\" 是想把匹配装入两个引号内，然后*在正则中的操作是贪婪的
# 因此匹配时基于找到最长可能匹配。所以第二个匹配 text2 中会错误的匹配两个引号内的东西
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# 修复如下，*后面加？强制执行短匹配   .的意思时匹配除了换行之外的所有字符
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))