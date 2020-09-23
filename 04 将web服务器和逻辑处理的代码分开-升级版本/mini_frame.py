# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/23 14:23
import time


def login():
    return "----login-----\r\nwelcome hhh to our website    time:%s" % time.ctime()


def register():
    return "----register-----\r\nwelcome hhh to our website    time:%s" % time.ctime()


def profile():
    return "----profile-----\r\nwelcome hhh to our website    time:%s" % time.ctime()


def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    else:
        return "not found you page...."
