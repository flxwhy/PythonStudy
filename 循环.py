# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5]:
    sum = sum+x
print(sum)

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
list(range(5))

# while循环
sum = 0
n = 99
while n > 0:
    sum = sum+n
    n = n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print(a)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n+1
print('END')

n = 0
while n < 10:
    n = n+1
    if n % 2 == 0:
        continue
    print(n)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n+1
print('END')
