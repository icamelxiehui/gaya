#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-06-02 10:32:30
@author xiehui
"""

import os
import sys

class BnsParser(object):
    """Get server ip and port from bns"""
    def __init__(self, bns_name):
        self.bns_name = bns_name

    def parserBns(self, bns_name):
        """get ip and port from bns"""
        cmd = "get_instance_by_service -arm " + bsn_name
        cmd = "get_instance_by_service -arm redis3proxy-mco-\
               grfeed.osp.tc:proxy_port | cut -d' ' -f2,4 | head -n 1"

        

        
