# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/25 15:26

# 不一样的函数进行不一样的验证
def set_level(a):
    def set_func(func):
        def call_func(*args, **kwargs):
            print("-----%s----" % a)
            return func()
        return call_func
    return set_func

@set_level("级别1")  # 传入参数的装饰器分两步进行      1. 将参数传入并调用函数
def test1():                                 #      2. 将函数返回的结果作为装饰器对下面的函数进行装饰
    print("-----test1-----")
    return "ok1"

@set_level("级别2")
def test2():
    print("-----test2-----")
    return "ok2"

test1()
test2()