#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/03 08:10:23
#   Desc    :
#
import pprint
import os.path

from tornado.log import gen_log
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

from core.manage import find_all_handlers


def get_settings():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.join(cur_dir, os.pardir)
    settings = {
        "template_path": os.path.join(parent_dir, "templates"),
        "static_path": os.path.join(parent_dir, "static"),
        "debug": True
    }
    return settings


def main():
    handlers = find_all_handlers("handlers")
    settings = get_settings()
    pprint.pprint(handlers)
    pprint.pprint(settings)
    app = Application(handlers, **settings)
    server = HTTPServer(app)
    server.bind(8888, "127.0.0.1")
    gen_log.info(server)
    server.start(1)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
