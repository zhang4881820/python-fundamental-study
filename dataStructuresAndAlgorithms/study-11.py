# 抽取字典类型中的子字典

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20,
          'FB': 10.75}
# 制造一个值大于200的字典. {}
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# 制造一个tech仓库 把prices里面的key与tech里面的相匹配的抽取放入tech中
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)
# 也可以用dict()函数操作
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)
# 注意用用字典方式也就是{} 第一种方式速度会快2倍