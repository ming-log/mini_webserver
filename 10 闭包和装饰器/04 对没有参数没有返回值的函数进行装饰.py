# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 15:09
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
