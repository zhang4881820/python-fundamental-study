# inp = input('输入一个字符: ')
# if ord(inp) > 80:
#     print('ASCII VALUE IS greater than 80')
# else:
#     print('ASCII value is less than 80')


# rows = input('输入行数: ')
# m = int(rows)
#
# for i in range(m):
#     for j in range(0, m-i-1):
#         print(" ", end="")
#     for k in range(0, 2*i+1):
#         print("*", end="")
#     print()


def product(num1, num2):
    prod = num1 + num2
    print(str(prod))


num1 = int(input('请输入第一个数字\t'))
num2 = int(input('请输入第二个数字\t'))
product(num1, num2)