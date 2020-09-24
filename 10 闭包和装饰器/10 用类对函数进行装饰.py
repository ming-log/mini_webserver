# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/24 17:32


class Test(object):
    def __init__(self, func):
        self.func = func  # 将接收的参数进行保存

    def __call__(self, *args, **kwargs):
        print("123123")
        return self.func()  # 调用接收的参数


@Test  # test = Test(test)  相当于对类进行实例化，传入的参数为test函数
def test():
    print("-----test-----")
test()
