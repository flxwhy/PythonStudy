# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，
# 使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d['Adam'])
# 不存在会报错
# print(d['json'])
# 判断是否存在
s = 'json' in d
print(s)
# get()返回null或指定值
print(d.get('json'))
print(d.get('json', -1))
# 删除key
d.pop('Adam')

print(d)
# dic和list比较 1.查找和插入的速度极快，不会随着key的增加而变慢；
# 2.需要占用大量的内存，内存浪费多
# dict是用空间来换取时间的一种方法。
# 需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
# 那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法

# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

# set和dict类似也是一组key的集合，但是没有value，由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)

# 重复元素在set中自动被过滤：
s = set([1, 1, 1, 2, 2, 3, 3])
# 添加元素
s.add(4)
# 删除元素
s.remove(4)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2
#可变对象
a=['c','b','a']
a.sort()
#不可变对象
a='abc'
a.replace('a','A')
print(a)
