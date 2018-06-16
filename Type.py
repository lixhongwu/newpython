#!usr/bin/python
# -*- coding: UTF-8 -*-
# 变量类型 number String list tuple（元组） dictionary （字典） bool
str = 'Hello World!'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
list[0] = 1
print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
list.append('Runoob') # 追加
del list[0]  # 删除
print list + tinylist  # 打印组合的列表

# 元组 不能二次赋值
tuple = ('runoob', 786, 2.23, 'john', 70.2)
# tuple[0] = 'ss' 不能再赋值
tinytuple = (123, 'john')

print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
# print tuple + tinytuple  # 打印组合的元组

print bool(1)