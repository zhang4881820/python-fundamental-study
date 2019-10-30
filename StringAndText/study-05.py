# 查找替换文本

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# 一些复杂的方式
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

# sub 第一个参数是正则匹配规则。第二个参数是替换的模式。
# 其中\3 代表捕获组的号码
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# 编译使用
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# 指定一个替代对象的回调方法,来实现替代
from calendar import month_abbr

def change_date(m):
    # 取月份的英文简写名字
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))

# 如果想要得到替换的次数那么使用subn 替换sub方法
new_text, n = datepat.subn(change_date, text)
print('subn替换后的新字符串：', new_text, '\n替换次数是:',n)

