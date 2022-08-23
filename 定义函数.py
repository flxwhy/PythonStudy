import math


def my_abs(x):
    # 参数类型异常检查
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型不正确')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))

# 空函数 如果想定义一个什么事也不做的空函数，可以用pass语句：


def nop():
    pass


# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass还可以用在其他语句里，比如：
age = 10
if age >= 18:
    pass


# 返回多个值 原来返回值是一个tuple！
# 返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，所以，
# Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi/6)
print(x, y)
r = move(100, 100, 60, math.pi/6)
print(r)

# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。
# 方程ax²+bx+c=0 求解
def quadratic(a, b, c):
    if a == 0:
        x1 = -c/b
        return x1
    elif b**2-4*a*c < 0:
        return '无解'
    else:
        x1 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        return x1, x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))