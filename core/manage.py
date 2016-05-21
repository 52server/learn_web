#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/03 15:14:04
#   Desc    :
#
import os
import inspect
import importlib

from tornado.web import RequestHandler


def route(pattern):
    def wrapper(handler):
        handler.__route__ = pattern
        return handler
    return wrapper


def find_module_handlers(module):
    handlers = []
    for m in module.__dict__.values():
        if inspect.isclass(m) and issubclass(m, RequestHandler) \
                and hasattr(m, "__route__"):
            handlers.append((m.__route__, m))
    return handlers


def find_all_handlers(dirname):
    handlers = []
    for f in os.listdir(dirname):
        if f.endswith(".py"):
            module = importlib.import_module(
                dirname.replace("/", ".") + "." + os.path.splitext(f)[0])
            handlers.extend(find_module_handlers(module))
    return handlers
