#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/20 18:51:20
#   Desc    :
#
import os
import uuid

from core.web import WebHandler
from core.manage import route
from core.util import get_qr_code_with_logo


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


@route("/learn/qrcode")
class LearnQrcodeHandler(WebHandler):
    def get(self):
        self.render("learn_qrcode.html")


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


@route("/qrcode/create")
class QrCodeCreateHandler(WebHandler):
    def post(self):
        data = self.get_argument("qr_data")
        logo_data = self.request.files["logo"][0]["body"]
        logo_name = self.request.files["logo"][0]["filename"]
        dir_ = os.path.join(os.path.dirname(__file__), "uploadpic")
        if not os.path.exists(dir_):
            os.mkdir(dir_)

        logo_path = os.path.join(dir_, str(logo_name))
        with open(logo_path, "w") as f:
            f.write(logo_data)

        im = get_qr_code_with_logo(data,  logo_path)

        qr_path = "static/pic/qrcode-{}.png".format(uuid.uuid1().hex)
        im.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             os.path.pardir, qr_path))
        self.write_success({
            "qr_path": os.path.join("/", qr_path)
        })
