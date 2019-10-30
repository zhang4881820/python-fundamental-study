# 文本模式的匹配搜索

# 直接上例子

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# \d表示匹配数字1个或多个
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# 进行预编译,如果要用同一个正则匹配多个数据·就可以预编译成一个正则对象
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')
# 查找匹配的字符串
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
# 接着咱们的捕获组方式 三个括号就是三组在加上本身就是4组,groups不会把本身算进去
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')# 这种匹配方式不是很准确。要想精确匹配，在结尾除加$
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
# 查找所有匹配·按照一定格式输出
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
# 看看加$和不加的区别
datepat_new = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012aaaaaaaaa').groups(),"接下来看加了$的能匹配不")
# 精确·不能匹配
print(datepat_new.match('11/27/2012aaaaaaaaa'))



