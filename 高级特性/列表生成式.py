# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
import os
list(range(1, 11))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for lis in list(range(1, 11)):
    L.append(lis*lis)


# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
[x*x for x in range(1, 11)]

# 写列表生成式时，把要生成的元素x * x放到前面，
# 后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

[x*x for x in range(1, 11) if x % 2 == 0]

# 还可以使用两层循环，可以生成全排列：

[m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 三层和三层以上的循环就很少用到了。

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
# os.listdir可以列出文件和目录
[d for d in os.listdir('.')]


# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

d = {'x': 'A', 'y': 'B', 'z': 'C'}

for k, v in d.items():
    print(k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list：
[k + '=' + v for k, v in d.items()]


# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

# ['hello', 'world', 'ibm', 'apple']

# 但是，我们不能在最后的if加上else：
# 这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？
# 另一些童鞋发现把if写在for前面必须加else，否则报错：
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果

[x if x % 2 == 0 else -x for x in range(1, 11)]


# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
