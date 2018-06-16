#!usr/bin/python
# -*- coding: UTF-8 -*-
# + - * / % **（幂运算） //取整数部分
print 2**3
print 9//4
print str(5.0/3)

# != == <> >=  <= > <

# 逻辑运算 and or not
if (1 and 0):
    print 'true'
else :
    print 'false'

# 成员运算 in ，not in
list = [1, '2', 3]
if (1 in list):
    print 'true'

# 身份运算 is  is not
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

print 2 is 2

# python 不支持switch 语句