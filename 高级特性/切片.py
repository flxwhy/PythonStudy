# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：
L[0:3]
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

# 如果第一个索引是0，还可以省略：
L[:3]

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：

# -2 到 0
L[-2:]


L[-2:-1]


# 记住倒数第一个元素的索引是-1

# 切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))

L[:10]

# 后10个数：
L[-10:]

# 前11-20个数：
L[10:20]

# 前10个数，每两个取一个：

L[:10:2]

# [0, 2, 4, 6, 8]

# 所有数，每5个取一个：

L[::5]

# 原样复制
L[:]


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
(0, 1, 2, 3, 4, 5)[:3]


# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
'ABCDEFG'[:3]

'ABCDEFG'[::2]

# 在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），
# 其实目的就是对字符串切片。Python没有针对字符串的截取函数，
# 只需要切片一个操作就可以完成，非常简单。


# 练习
def trims(str):
    if str != '':
        while str[0] == ' ' and len(str) > 1:
            str = str[1:]
        while str[-1:] == ' ' and len(str) > 1:
            str = str[:-1]
        if str == ' ':
            str = ''
    return str


# 优化版 最少切片次数
def trimsd(str):
    lens = len(str)
    if lens <= 0 or str == ' ' or str == '':
        return ''
    searchindex = 0
    while lens > searchindex:
        if(str[searchindex] == ' '):
            searchindex += 1
        else:
            break
    lens -= 1
    while lens > 0:
        if(str[lens] == ' '):
            lens -= 1
        else:
            break
    return str[searchindex:lens+1]
trimsd('   sdsd     ')
