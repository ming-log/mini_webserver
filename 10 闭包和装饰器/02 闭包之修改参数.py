# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 14:54
x = 300
def test1():
    x = 200
    def test2():
        nonlocal x
        print("---1--- x=%d" % x)
        x = 100
        print("---2--- x=%d" % x)
    return test2

t = test1()
t()
