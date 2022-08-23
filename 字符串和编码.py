# python3 字符串是以Unicode编码
print('包含中文的str')
# 字符转编码例子
print(ord('A'))
print(ord('中'))
# 编码转字符串
print(chr(66))
print(chr(25991))
# 整数编码
print('\u4e2d\u6587')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示

x = b'ABC'
b = 'ABC'.encode('ascii')
d = '中文'.encode('gb2312')
c = '中文'.encode('utf-8')
# d='中文'.encode('ascii')
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，
# 含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，
# 因为中文编码的范围超过了ASCII编码的范围，Python会报错。
len('ABC')
len('中文')

len(b'\xe4\xb8\xad\xe6\x96\x87')

# 字符串格式化

# 占位符分为    %d 整数     %f 浮点数    %s 字符串  %x 十六进制整数
# 其中格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# format() 不常用
'Hello, {0},成绩提升了{1:.1f}%'.format('小明', 17.125)

# f-string
r = 2.5
s = 3.14*r**2
print(f'The area of a circle with radius {r} is {s:.2f}')

'提升了 %.1f' % (1-72/85)