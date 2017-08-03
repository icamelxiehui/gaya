#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-06-01 11:54:54
@author xiehui
"""

import os
import sys

class Path(object):
    """class to deal with path"""
    def  __init__(self, root):
        self._root = root
    
    def abspath(self, path):
        """add path to root"""
        return os.path.join(self._root, path)
    
    def root(self):
        """get root"""
        return self._root


__g_path_table = {}


def create_path(name, root):
    """Add path to globle path table"""
    __g_path_table[name] = Path(root)


def path(name):
    """get path by name"""
    return __g_path_table[name]    


def include(path):
    """add path to system"""
    sys.path.append(path)


def remove(path):
    """remove path from system"""
    try:
        sys.path.remove(path)
    except Exception as e:
        print "remove %s error: %s" % (path, e)





