'''

不能随便空格每个空格都有它的意义 
 默认四个空格  
一般直接结尾，不以分号结尾
一行不会放置多条语句
万物皆对象，函数也可以当对象
有些代码的不想运行 但又不想删除可以用# 注释掉，相运行再加上
每个文件的后缀名就叫 py
a==b结果为true 一个等号就变成了语义赋值了
if 与 else   if与else都是并列的关系
for循环不需要 end结尾
'''
import numpy as np
import pandas as pd
from pandas import DataFrame
# a=("请输入文字")
# '''
# print(a)
# type(a)
# print(type(a))
# for b in [3,4.4,'life']: #for直接循环就可以结束 不需要end
#     print (b)
# idx = range(5)
# print (idx)
#
# def square_sum(a,b):# def表示定义函数名 square_sum是函数名可以自己命名
#     c = a**2 + b**2# 函数内部计算的方法自己定义
#     return (c)
#     print (square_sum(3,4))
# a = 1

# def change_integer(a):
#     a = a + 1
#     return a
#
# print change_integer(a)
# print a

#===(Python中 "#" 后面跟的内容是注释，不执行 )
#
# b = [1,2,3]
#
# def change_list(b):
#     b[0] = b[0] + 1
#     return b
#
# print change_list(b)
# print b
#
# dic = {'tom':11, 'sam':57,'lily':100}

# print (type(dic))
# print (dic)
# dic['tom']=30#通过健来索引 将位置改了参数
# print (dic)
# dic['lilei'] = 99
# print (dic) #网站上的书好，看完可以直接实验 便于理解
# dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
# for key in dic:
#     print (dic[key])
# print (dic.keys() )
# print (dic.values() )
# print (dic.items())#返回所有值
# del dic['tom']
# print (dic)
#
# def f(a,b,c):
#     return a+b+c#自己看错了  return与def合用 return就是这个函数最后要 输出的值
#
# print(f(1,2,3))
# print(f(2,c=3,b=2))#重点是里面这三个数相加 具体怎么加没有关系
# def f(a,b,c=10):
#     return a+b+c
#
# print(f(3,2))
# print(f(3,2,1))
#
# def func(**dict):
#     print (type(dict))
#     print (dict)
#
# func(a=1,b=9)
# func(m=2,n=1,c=11)
#
# def func(a,b,c):
#     print (a,b,c)#相当于 这个函数本来就要输出的 都是这个函数的一部分
#
# args = (1,3,4)
# func(*args)
# dict = {'a':1,'b':2,'c':3}
# func(*dict)
#
# S = 'abcdefghijk'
# print(len(S))#就是长度的意思
# for i in range(0,len(S),2):
#     print (S[i])
#
# S = 'abcdefghijk'
# for (index,char) in enumerate(S):
#    # print (index)位置 从0开始
#    print (char)#一个一个循环里面的元素  index是元素的位置，char是元素的内容
#
# ta = [1, 2, 3]
# tb = [9, 8, 7]
# tc = ['a', 'b', 'c']
# for (a, b, c) in zip(ta, tb, tc):#zip函数每次只取一个元素
#     print(a, b, c)
#
# ta = [1,2,3]
# tb = [9,8,7]
#
# # cluster
# zipped = zip(ta,tb)
# print(zipped)
#
# # decompose
# na, nb = zip(*zipped)
# print (na, nb)
# def gen():
#     a = 100
#     yield a
#     a = a*8
#     yield a
#     yield 1000

# L = [x**2 for x in range(10)]#每个数的平方  不用print也可以直接看变量
# xl = [1,3,5]
# yl = [9,12,13]
# L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
# func = lambda x,y: x + y
# print (func(3,4))
# def func(x, y):
#     return x + y
# print(func(2, 3))
# def test(f, a, b):
#     print ('test')
#     print (f(a, b))#f代指func
# test(func, 3, 5)
# test((lambda x,y: x**2 + y), 6, 9)#后面两个数相当于x y和ab 的关系
# re = map((lambda x: x+3),[1,3,5,6])
# re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
# def func(a):
#     if a > 100:
#         return True
#     else:
#         return False
# print(func,[10,56,101,500])
# print (filter(func,[10,56,101,500])) #上面是定义函数 下面是运行函数 定义函数的对象颜色是比较深的，真正运行的代码是比价浅的
# print (reduce((lambda x,y: x+y),[1,2,5,7,9]))

L1 = [1,2,3]
L2 = L1
L1[0] = 10
print (L2)