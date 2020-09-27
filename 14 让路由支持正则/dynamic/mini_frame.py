# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/23 14:23
import re
from pymysql import connect

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


@route(r"/index.html")
def index(ret):
    with open("./templates/index.html", encoding='utf-8') as f:
        content = f.read()
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='123456', charset='utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    info_data = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = ""
    for i in info_data:
        tr_template += """<tr>
                    <td>%d</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>
                        <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                    </td><tr>
        """ % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[1])
    content = re.sub(r"\{%content%\}", tr_template, content)
    return content


@route(r"/center.html")
def center(ret):
    with open("./templates/center.html", encoding='utf-8') as f:
        content = f.read()
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='123456', charset='utf8')
    cs = conn.cursor()
    cs.execute("select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i "
               "right join focus as f on i.id = f.info_id;")
    info_data = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = ""
    for i in info_data:
        tr_template += """<tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>
                        <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> 
                        <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                    </td>
                    <td>
                    <input type="button" value="删除" id="toDelete" systemidvalue="%s">
                    </td><tr>
        """ % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[0], i[0])
    content = re.sub(r"\{%content%\}", tr_template, content)
    return content


# 给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数，例如/add/000007.html中000007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加 url对应的函数 到字典中，此时字典中的键值对有N个，浪费空间
# 而采用了正则的话，那么只要编写1次@route就可以完成多个 url例如/add/00007.html /add/000036.html等对应同一个函数，
# 此时字典中的键值对个数会少很多
@route(r"/add/(\d+)\.html")
def add_foucus(ret):
    stock_code = ret.group(1)
    return "add    (%s) ok ...." % stock_code


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']
    # if file_name in URL_FUNC_DICT.keys():
    #     func = URL_FUNC_DICT[file_name]
    #     return func()
    # else:
    #     return 'Hello World!  窗口点击关闭'
    try:
        # return URL_FUNC_DICT[file_name]()
        # 当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，没有则继续执行后续代码
        for url, func in URL_FUNC_DICT.items():
            print("url:", url)
            print("func:", func)
            print("file_name:", file_name)
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数..." % file_name
    except Exception as e:
        return "产生了'%s'异常" % e
