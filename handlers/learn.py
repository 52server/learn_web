#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/20 18:51:20
#   Desc    :
#

import os

from core.web import WebHandler
from core.manage import route


@route("/learn")
class LearnHandler(WebHandler):
    def get(self):
        self.render("learn.html")


@route("/learn/edit")
class LearnEditHandler(WebHandler):
    def get(self):
        self.render("learn_edit.html")


@route("/learn/slider")
class LearnSliderHandler(WebHandler):
    def get(self):
        self.render("learn_slider.html")


@route("/learn/carousel")
class LearnCarouselHandler(WebHandler):
    def get(self):
        self.render("learn_carousel.html")


@route("/learn/bootstrap")
class LearnBootstrapHandler(WebHandler):
    def get(self):
        self.render("learn_bootstrap.html")


@route("/learn/upload")
class LearnUploadHandler(WebHandler):
    def post(self):
        dir_ = os.path.join(os.path.dirname(__file__), "uploadpic")
        if not os.path.exists(dir_):
            os.mkdir(dir_)
        for k, item_list in self.request.files.items():
            print("-----------key: %s----------" % k)
            for item in item_list:
                print(item["filename"])
                # print(item["body"])
                print(item["content_type"])
                with open(os.path.join(dir_, str(item["filename"])), "w") as f:
                    f.write(item["body"])
        self.render("learn_upload.html")
