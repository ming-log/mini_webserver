# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 15:09

def set_func(func):
    def call_func(num):
        print("-----这是权限验证1-----")
        print("-----这是权限验证2-----")
        func(num)
    return call_func

@set_func  # 相当于test1=set_func(test1)
def test1(number):
    print("----test1---- %d" % number)

test1(14)
test1(1244)