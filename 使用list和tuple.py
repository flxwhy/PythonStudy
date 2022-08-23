classmates=['Michael','Bob','Tracy']
#获取长度
len(classmates)
#添加元素
classmates.append('Adam')
#插入指定位置
classmates.insert(1, 'Jack')
#删除末尾元素
classmates.pop()
#删除指定位置元素
classmates.pop(1)
#替换元素直接赋值
classmates[1] = 'Sarah'
#对比一般编译型语言 不同的是list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
#拆开写
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
#没有元素
L = []
len(L)


#元组   tuple
#tuple和list非常类似，但是tuple一旦初始化就不能修改
#它也没有append()，insert()这样的方法。
classmates = ('Michael', 'Bob', 'Tracy')

#可以定义空的tuple
t = ()

#有种特殊情况 如果定义一个元素
t = (1)
#这样就不是tuple 是1这个数，因为括号() 既可以表示tuple，又可以表示数学公式中的小括号 
#正确定义
t = (1,)

#让tuple可变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
#其实就是改变引用成员值

