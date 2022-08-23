# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# 对于函数的调用者来说，只需要知道如何传递正确的参数，
# 以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，
# 调用者无需了解。

# 位置参数
def power(x):
    return x*x


power(5)

# 改良成n次方


def power(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

# 可选参数


def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。


def add_end(L=[]):
    L.append('END')
    return L


add_end()
# 每次执行 add_end（）会改变默认参数 L 默认参数应该指向不变对象

# 正确更改


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# str、None 为不变对象，str相当于特殊处理的


def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

# 可变参


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum


nums = [1, 2, 3]
# *解构
calc(*nums)


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
