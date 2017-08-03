#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-06-01 14:25:05
@author xiehui
"""

import importlib
import sys

def loadmodule(name):
    """load module base on module name"""
    return importlib.import_module(name)


def loadclass(packname, classname):
    """get class from module"""
    module = loadmodule(packname)
    if module is None:
        return None
    return getattr(module, classname)    


def releasemodule(packname):
    """remove module from sys"""
    if packname in sys.modules:
        return sys.modules.pop(packname)
    return 0
    

