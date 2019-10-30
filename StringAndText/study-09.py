# 规范标准化 unicode 文本

# 带有unicode 的字符串
# 两种形式的Jalapeño ，s1完整的组成了“ñ”，
# s2的n结合了Unicode中的‘~’并连接字符0303
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print('\u00f1o')
print('\u0303o')
print(s1, '长度是:', len(s1))
print(s2, '长度是:', len(s2))

# 可以看出这种多种形式的字符 ，会存在问题。
# 可以使用unicodedata 模块 修复


import unicodedata
# NFC 意思是这个字符串应该被完整的组合
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1), '\n', ascii(t2))
# 可以看出 NFD 就是使用结合的方式··u0303o'
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s1)
print(ascii(t3), '\n', ascii(t4))

s = '\ufb01'
print(s)
# 使用结合方式·连结在一起
t5 = unicodedata.normalize('NFD', s)
print(t5)
# NFKD，NFKC 这两种方式就是把结合的unicode字符打破分离开
t6 = unicodedata.normalize('NFKD', s)
t7 = unicodedata.normalize('NFKC', s)

print(t6, '\n', t7)

# 这个例子展示使用unicodedata模块的另一个函数combining（）
# 这个函数就是测试传入的字符串是否是一个结合字符 这里面 ‘~’这是个结合字符
t1 = unicodedata.normalize('NFD', s2)
a = ''.join(c for c in t1 if not unicodedata.combining(c))
print(a)