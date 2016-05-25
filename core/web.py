#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/03 15:16:02
#   Desc    :
#
import json

import jinja2

from tornado.web import RequestHandler
from tornado.web import gen_log


class WebHandler(RequestHandler):
    def render_string(self, template_name, **kwargs):
        template_path = self.get_template_path()
        gen_log.debug("Template path: {}".format(template_path))

        loader = jinja2.FileSystemLoader(template_path)
        env = jinja2.Environment(loader=loader)
        template = env.get_template(template_name)
        ns = self.get_template_namespace()
        ns.update(**kwargs)

        return template.render(**ns)

    def write_success(self, data):
        data.update({"success": True})
        self.write(json.dumps(data))
