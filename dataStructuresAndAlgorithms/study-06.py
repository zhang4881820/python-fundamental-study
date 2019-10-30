words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
         'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're",
         'under']
from collections import Counter
# 找出重复次数前三的元素
word_counts = Counter(words)
top_three = word_counts.most_common(3)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
print(top_three)

# 数单个
print(word_counts['not'])
# 扩展一些新元素去数
more_worlds = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# 第一种方式
for word in more_worlds:
    word_counts[word] += 1
print(word_counts['not'])
# 第二种方式
word_counts.update(more_worlds)
print(word_counts['not'])
# 一个小特性
a = Counter(words)
b = Counter(more_worlds)
print(a)
print(b)
# 结合两个计数
c = a + b
print(c)
# 两个计数相减
c = a - b
print(c)

