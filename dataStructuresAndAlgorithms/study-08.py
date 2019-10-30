# 对象比较
class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

print(User(23))
users = [User(23),User(3),User(99)]
users_lambda_sorted = sorted(users, key=lambda u: u.user_id)
print(users_lambda_sorted)

# 使用 alternative 替换lambda表达式 用来提取对象属性
# 也可以传入多个参数基本雷同列表取key的itemgetter
from operator import attrgetter
users_attr_getter_sorted = sorted(users, key=attrgetter('user_id'))
print(users_attr_getter_sorted)
