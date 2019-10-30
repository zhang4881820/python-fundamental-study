# 净化，清洁文本

# 清洁下面的字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
# 首先清楚一下空格那些，使用translation 表 然后translate()
remap = {
	ord('\t'): ' ',
	ord('\f'): ' ',  # 单空格替换
	ord('\r'): None  # 删除的意思
}
a = s.translate(remap)
print(a)
# 接下来解除所有的combine（结合的）字符
import unicodedata
import sys

# 这个代码的意思就是找出Unicode中的combine结合字符。然后组装成key ： value的字典类
# 这里的value是none
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
print(a.translate(cmb_chrs))
# 将字符串规范化·NFD 使之进入decomposed（分化） 形式
b = unicodedata.normalize('NFD', a)
print(b)
# 然后就匹配combine字符开始一顿删除
print(b.translate(cmb_chrs))
# 还有一种方式 是设计i/o的编码解码的
print(a)
# 首先通过normalize把字符串变成一种携带分离字符的字符
# 随后的ASCII编码/解码简单的去除分离掉落下来的字符 （因为很简单连接字符的值肯定超过ascii码的值最大255）
# 当然你要的目标字符他必须在ASCII码范围内。。
b = unicodedata.normalize('NFD', a)
b = b.encode('ascii', 'ignore').decode('ascii')
print(b)
# 翻译Unicode的10进制数字

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# 值得一说的是str.replace() 替换的速度比translate（）快·即使是多次使用replace
# 但是某些方面translate 的速度会快比如一些不重要的字符对字符的映射或者删除
