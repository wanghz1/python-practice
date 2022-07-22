# 位置实参
def fun(a, b):
    print(a, b)


print('位置实参')
fun(10, 20)
# 关键字实参
print('关键字实参')
fun(a=10, b=20)


# 将序列中的元素转换为位置实参
def fun1(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)


print('列表转换位置实参')
lst = [10, 20, 30]
fun1(*lst)  # 使用*转换列表中的元素

print('字典转换关键字实参')
dis = {'a': 100, 'b': 200, 'c': 300}
fun1(**dis)  # 使用**转换字典中的键值对


# 默认值实参
def fun2(a, b=10):  # 在函数定义处，形参b被赋值，称为默认值形参
    print(a, b)


print('默认值实参')
fun2(20)


'''
可变的位置参数只能定义一个
可变的关键字参数只能定义一个
函数定义中，有两个可变的参数时，位置参数要放在关键字参数前面
'''


# 可变个数的位置实参
def fun3(*a):
    print(a)


print('可变个数的位置实参')
fun3(10, 20)  # 结果为元组


# 可变个数的关键字实参
def fun4(**b):
    print(b)


print('可变个数的关键字实参')
fun4(a=10, b=20, c=30)  # 结果为字典
