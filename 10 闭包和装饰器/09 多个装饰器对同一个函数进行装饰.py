# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 17:32


def set_func1(func):
    print("开始装饰set_fun1")
    def call_func():
        print("-----调用set_func1函数-----")
        func()
        print("-----调用完毕set_func1函数-----")
    return call_func


def set_func2(func):
    print("开始装饰set_fun2")
    def call_func():
        print("-----调用set_func2函数-----")
        func()
        print("-----调用完毕set_func2函数-----")
    return call_func


@set_func2
@set_func1
def test():
    print("------test 函数-----")


test()
