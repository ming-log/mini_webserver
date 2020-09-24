# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 17:18


def set_func(func):
    def call_func(*args, **kwargs):
        print("-----这是权限验证1-----")
        print("-----这是权限验证2-----")
        # func(args, kwargs)  # 不行，相当于传递了2个参数；1个元组，1个字典
        return func(*args, **kwargs)  # 拆包, 加了return不影响不需要返回值的函数
    return call_func


@set_func  # 相当于test1=set_func(test1)
def test1(number, *args, **kwargs):
    print("----test1---- %d" % number)
    print("----test1---- ", args)
    print("----test1---- ", kwargs)
    return "ok"


@set_func
def test2():
    pass


ret = test1(100)
print(ret)

ret = test2()
print(ret)
