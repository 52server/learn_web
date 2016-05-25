#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author  :   swolf.qu
#   E-mail  :   swolf.qu@gmail.com
#   Date    :   2016/05/25 11:31:48
#   Desc    :
#
from PIL import Image

from qrcode.main import QRCode
from qrcode.constants import ERROR_CORRECT_M


def image_resize(name, width):
    image = Image.open(name)
    wpercent = width/float(image.size[0])
    height = int(float(image.size[1]*wpercent))
    image = image.resize((width, height), Image.ANTIALIAS)
    return image


def get_qr_code(data, **kwargs):

    im_name = kwargs.pop("image", None)

    qr = QRCode(**kwargs)
    qr.add_data(data)
    qr_image = qr.make_image()
    if im_name:
        im = image_resize(im_name, 40)
        x = qr_image.size[0]/2 - im.size[0]/2
        # If the modes don’t match, the pasted image is converted to the mode of
        # this image.
        # The qr_image mode is 1, the im mode is RGB,
        # We must convert the mode first to let the im looks colorful.
        qr_image = qr_image.convert(im.mode)
        qr_image.paste(im, (x, x))
    return qr_image


def get_qr_code_with_logo(data, logo_path):
    kwargs = {
        "version": 1,
        "error_correction": ERROR_CORRECT_M,  # L M Q H
        "box_size": 10,
        "border": 4,
        "image": logo_path
    }

    return get_qr_code(data, **kwargs)
