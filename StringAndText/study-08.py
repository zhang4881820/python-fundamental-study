# 多行模式编写正则表达式
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '/* this is a \n ' \
		'multiline comment */'
print(text2)
print(comment.findall(text1))
# .就是不匹配换行 ，所以匹配不到
print(comment.findall(text2))

# 修复方法 ?:不捕获组。意思就是定义一个以匹配为目的的组。但是不对这个组进行分离捕获
# 也就是括号内的内容将被捕获
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))
# re.compile() function 接受一个flag DOTALL这个标志就是使.可以匹配新行的··
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
# 简单的正则使用flag没问题。但是复杂的正则，比如混合多个单独的正则
# 使用标记的时候会出现问题，那种情况最好别使用额外的标记