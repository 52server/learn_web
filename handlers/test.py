#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/03 15:12:01
#   Desc    :
#
from core.web import WebHandler
from core.manage import route


@route("/hello")
class HelloHandler(WebHandler):
    def get(self):
        # self.write("Hello")
        context = {
            "title": "hello",
            "body": "beijing"
        }
        self.render("hello.html", **context)


@route("/index")
class HomeHandler(WebHandler):
    def get(self):
        self.render("index.html")
