#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/03 08:10:23
#   Desc    :
#
from __future__ import print_function

import pprint
import os.path

from tornado.log import gen_log
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import parse_command_line

from core.manage import find_all_handlers

HOST = "127.0.0.1"
# HOST = "192.168.1.100"
PORT = 8888


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
    parse_command_line()

    handlers = find_all_handlers("handlers")
    settings = get_settings()

    # Enable debug log.
    # Tornado set the log level to INFO default.
    if settings.get("debug", False):
        gen_log.setLevel("DEBUG")

    pprint.pprint(handlers)
    pprint.pprint(settings)

    app = Application(handlers, **settings)
    server = HTTPServer(app)
    server.bind(PORT, HOST)
    print("Server run at " + HOST + ":" + str(PORT))

    server.start(1)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
