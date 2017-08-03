#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-05-27 15:07:19
@author xiehui
"""
import os
import sys

ROOT_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
reload(sys)     
sys.setdefaultencoding('utf8')
sys.path.append(ROOT_DIR)

import lib.path
lib.path.create_path("ROOT_DIR", ROOT_DIR)

from framework import Framework

if __name__ == "__main__":
    framework = Framework()
    framework.start()
