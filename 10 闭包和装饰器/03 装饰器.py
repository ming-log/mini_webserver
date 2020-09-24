# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 15:09

def test1():
    print("----test1----")

test1()
# >>>----test1----


def set_func(func):
    def call_func():
        print("-----这是权限验证1-----")
        print("-----这是权限验证2-----")
        func()
    return call_func

@set_func
def test1():
    print("----test1----")

test1()
# >>>-----这是权限验证1-----
# >>>-----这是权限验证2-----
# >>>----test1----
# 装饰器可以在不改变原始函数的 内容 和 调用方式 的前提下对函数添加功能，
# 但是只能在整体前面加或者整体后面加，不能在原来函数的中间添加功能
