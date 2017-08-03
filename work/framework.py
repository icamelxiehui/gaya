#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-05-27 15:07:19
@author xiehui
"""

import os
import zerorpc
import ConfigParser
import time
import lib.loggingmodule
import lib.tderr
import lib.loader
import json
from lib.mongo.mongotable import MongoTable

class Framework(object):
    def __init__(self):
        """init"""

        self.config = ConfigParser.ConfigParser()
        self.log_module = lib.loggingmodule.LoggingModule()
        self.config_file = lib.path.path("ROOT_DIR").abspath("conf/local.ini")

        cur_time = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        self.log_module.init_log("./log/local.%s" % cur_time)
        os.system('find log -mtime 60 -name "*.*" -exec rm -rf {} \;')     

    def load(self):
        """Load config file"""
        
        self.log_module.info("load config start")
        if len(self.config.read(self.config_file)) == 0:
            print "cc",self.config_file
            self.log_module.error("load config file %s failed!" % self.config_file)
            return lib.tderr.TD_ERROR_FAILTRUE

        self.log_module.info("local_config_file:%s sucess" % self.config_file)
        
        self.mongo = MongoTable(self.config, self.log_module)
        return lib.tderr.TD_OK


    def start(self):
        """start"""

        rv = self.load()
        if lib.tderr.FAILED(rv):
            return rv

        rv = self.process()
        if lib.tderr.FAILED(rv):
            return rv

    def process(self):
        """Start the process"""
        self.log_module.info("start process")

        process_list = self.config.get("task", "process_list")
        process_list = process_list.split(",")

        input_data = {}
        for process_name in process_list:
            process_name = process_name.strip()

            lib.path.include(lib.path.path("ROOT_DIR").abspath("plugin/"+process_name))
            packname = self.config.get(process_name, "pack_name")
            classname = self.config.get(process_name, "class_name")

            if packname  and classname:     
                ProcessClass = lib.loader.loadclass(packname, classname)
                if ProcessClass is None:
                    self.local_log_module.error("loadclass %s.%s failed!" % (packname, classname))
                    return lib.tderr.TD_ERROR_FAILTRUE

                processer = ProcessClass(self.config, self.log_module, self.mongo)
                rv = processer.process(input_data)
                if lib.tderr.FAILED(rv):
                    self.log_module.warning("processer.process failed") 
                    return lib.tderr.TD_ERROR_FAILTRUE

        return lib.tderr
