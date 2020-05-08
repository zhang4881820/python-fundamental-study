# 基本类型

## Numbers
1. Integer 整数
2. Floating point numbers 小数
3. complex numbers 复杂数
4. Decimal 固定精度的数
5. Ration 有理数
6. sets 数学集的抽象

## math库常用方法
1. ceil: 向上取整
2. floor: 向下取整
3. copysign: 第二个参数的符号和第一个参数一起返回.math.copysign(2,-0) ,返回-2.0
4. fabs: 取绝对值
5. factorial: 阶乘

## fractions库
具体操作在**Math_basic**文件中. 功能就是把数字变成最简的分数形式.注意一个参数的时候最好用单引号把参数
包裹起来

## Strings
String是包含字符的预定义对象.不可变对象.可以通过索引形式找出一个个字符.例如:
```
name = 'zhanglong'
print(name[0])
z
```
索引还可以往后面开始走,加`-`就可以了:
```
print(name[-2])
n
```
根据索引截取一段字符,通过`:`来搞定:
```
print(name[2:])
angbo
```
`len(name)`这个函数可以得出字符串的字符个数. 还可以通过`+`操作来结合其他字符串.可以通过数字
加`*`来指定字符串的重复次数并返回合并重复字符串的字符串.

## Lists 和 tuples

### lists
对象的列表集合,列表是可变的
+ 列表可以是同类型元素的集合:`[1,2,3]`
+ 列表也可以包含不同类型的元素:`[1,"abc",2.4]`
+ 列表可为空:`[]`
+ 列表里面可以包含列表.

列表的元素可以通过索引来访问.这和String通过索引访问字符是一样的

### tuples
元组对于数据交换特别有用.一个元组包含的元素可以单独使用或当作一个组.他也可以包含不同类型的
数据.
**特性**
+ 元组是不可变的

# 条件语句
    1. if
       if<条件>:
         <语句块>
    2. if-else
        if<条件>:
         <语句块>
        else:
         <语句块>
    3. If else ladder
       if<条件>:
         <语句块>
        elif<条件2>:
         <语句块> 
        elif<条件3>:
          <语句块> 
        else:  
          <语句块>
          
# 循环
提供两种:
1. while
>while 条件 :<br>
>else:
2. for
>for i in range(a,b):

# 函数FUNCTION
> 函数是一种执行指定任务.

看一个定义函数调用函数的例子:
```python
def product(num1, num2):
    prod = num1 + num2
    print(str(prod))

num1 = int(input('请输入第一个数字\t'))
num2 = int(input('请输入第二个数字\t'))
product(num1, num2)
```




