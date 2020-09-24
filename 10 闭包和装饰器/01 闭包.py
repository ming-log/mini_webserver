# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 13:44

# 问题：以y=kx+b为例，给定x求y

# 第一种
# k = 1
# b = 2
# y = k*x + b

# 第二种 封装函数
def line_2(k, b, x):
    print(k*x+b)
line_2(1, 2, 0)
line_2(1, 2, 1)
line_2(1, 2, 2)
# 缺点：如果需要计算多次这条线上的y值，那么每次都要传递k，b的值，麻烦

# 第三种 全局变量
k = 1
b = 2
def line_3(x):
    print(k*x+b)
line_3(0)
line_3(1)
line_3(2)
k = 11
b = 22
line_3(0)
line_3(1)
line_3(2)
# 缺点：如果要计算多条线上的y值，那么需要每次对全局变量进行修改，代码会增多，麻烦

# 第四种 缺省参数
def line_4(x, k=1, b=2):
    print(k*x+b)
line_4(0)
line_4(1)
line_4(2)
line_4(0, k=11, b=22)
line_4(1, k=11, b=22)
line_4(2, k=11, b=22)
# 优点：比全局变量的方式好在：k，b是函数line_4的一部分，而不是全局变量，因为全局变量可以任意的被其他函数修改
# 缺点：如果要计算多条线上的y值，那么需要在调用的时候进行传递参数，麻烦

# 第五种 实例对象
class Line(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        return self.k*x+self.b

line_5 = Line(1, 2)
line_5(0)
line_5(1)
line_5(2)
line_6 = Line(11, 22)
line_6(0)
line_6(1)
line_6(2)
# 缺点：为了计算多条线上的y值，所以需要保存多个k，b的值，因此用了很多个实例对象，浪费资源

# 第六中 闭包
def Line(k, b):
    def cal(x):
        return k*x+b
    return cal

line_7 = Line(1, 2)
line_7(0)
line_7(1)
line_7(2)
line_8 = Line(11, 22)
line_8(0)
line_8(1)
line_8(2)

# 思考：函数、匿名函数、闭包、对象当做实参时  有什么区别？
# 1. 匿名函数能够完成基本的简单功能，，，传递是这个函数的引用    只有功能
# 2. 普通函数能够完成较为复杂的功能，，，传递是这个函数的引用    只有功能
# 3. 闭包能够完成较为复杂的功能，，，传递是这个闭包的函数以及数据，因此传递是功能+数据
# 4. 对象能够完成最为复杂的功能，，，传递是很多数据+很多功能，因此传递的是功能+数据
