#!usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: 文件的操作
# @author lixhongwu@163.com
# @create 2018-06-18 9:59

# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
# str = raw_input('请输入：')
# print "你输入的是 ",str
ob = open('data.txt','r')
#ob.write('\n haolle')
print(ob.read(10))
# 查找当前位置
position = ob.tell()
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = ob.seek(0, 0)
str = ob.read(10)
print "重新读取字符串 : ", str
print ob.name
print ob.mode
ob.close()
