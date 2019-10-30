# 格式化字符

text = 'Hello World'
# 左右宽度调正,居中
print(text.ljust(20), 'a')
print(text.rjust(20))
print(text.center(20))
# 还可以指定填充字符
print(text.center(20, '*'))

# 还可以使用fomat() 方法来玩 主要三个字符：<（左边）,>(右边),^(居中)
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
# 当然也能加字符填充
print(format(text, '*^20'))
# 还可以这么玩 往format里面传多个字符串· 排序规则放前面
print('{:*>30} {:>10s}'.format('Hello', 'World'))

# format 这方法的好处是·不限于String,任何值
# 下面处理下数值
x = 1.23456
print(format(x, '>10'))
print(format(x, '>10.2f'))
