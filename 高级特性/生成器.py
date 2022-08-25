# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

L = [x*x for x in range(10)]

# g 就是一个generator
g = (x*x for x in range(10))

# 可以通过next()函数获得generator的下一个返回值：
next(g)

# 我们讲过，generator保存的是算法，每次调用next(g)，
# 就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：

for n in g:
    print(n)


# 所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误


# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现

# 斐波拉契数列
# 1, 1, 2, 3, 5, 8, 13, 21, 34  除第一个和第二个数外，任意一个数都可由前两个数相加得到

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1


fib(6)

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

# 这就是定义generator的另一种方法。如果一个函
# 数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
# 而是一个generator函数，调用一个generator函数将返回一个generator：

# 这里，最难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函数

# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 举个简单的例子，定义一个generator函数，依次返回数字1，3，5：


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield 5


o = odd()
next(o)

# 可以看到，odd不是普通函数，而是generator函数
# 在执行过程中，遇到yield就中断，下次又继续执行
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

# 这样调用永远返回1 因为多个实例总是执行第一步
next(odd())

for n in fib(6):
    print(n)
