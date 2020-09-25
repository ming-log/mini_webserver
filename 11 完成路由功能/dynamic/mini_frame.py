# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/23 14:23


def index():
    with open("./templates/index.html", encoding='utf-8') as f:
        content = f.read()
    return content


def center():
    with open("./templates/center.html", encoding='utf-8') as f:
        return f.read()


URL_FUNC_DICT = {
    "/index.py": index,
    "/center.py": center
}


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == '/center.py':
    #     return center()
    # else:
    #     return 'Hello World!  窗口点击关闭'
    func = URL_FUNC_DICT[file_name]
    return func()

