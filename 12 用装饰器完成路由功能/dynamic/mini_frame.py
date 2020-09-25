# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/23 14:23

# 利用装饰器完成字典内容
# 利用了装饰器的运行机制，运行到@符号位置就会进行装饰，而不是等到函数被调用才装饰
URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.py")
def index():
    with open("./templates/index.html", encoding='utf-8') as f:
        content = f.read()
    return content


@route("/center.py")
def center():
    with open("./templates/center.html", encoding='utf-8') as f:
        return f.read()


print(URL_FUNC_DICT)


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if file_name in URL_FUNC_DICT.keys():
    #     func = URL_FUNC_DICT[file_name]
    #     return func()
    # else:
    #     return 'Hello World!  窗口点击关闭'
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as e:
        return "产生了%s异常" % e
