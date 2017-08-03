#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: mongotable.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 二  6/27 09:50:31 2017
"""

import ConfigParser
import lib.loggingmodule
import lib.tderr
from pymongo import MongoClient

class MongoTable:
    
    def __init__(self, config, log_module):
        """init"""

        self.config = config
        self.log_module = log_module
        self.ip = config.get("mongo", "ip")
        self.port = int(config.get("mongo", "port"))
        self.client = MongoClient(self.ip, self.port)

    def seting(self, db_name, table_name):
        """set"""
    
        self.db = self.client[db_name]
        self.table = self.db[table_name]
        return lib.tderr.TD_OK

    def find_all(self):
        return self.table.find()

    def find_keyword(self, field, keyword):
        """find"""
        return self.table.find({field: {'$regex':keyword}})
        #return self.table.find({field: /keyword/})

    def find_one(self, condition):
        """find one"""
        return self.table.find_one(condition)

    def find(self, condition):
        """find condition"""
        return self.table.find(condition)


    def save(self, data):
        """save"""
        self.table.save(data)
        return lib.tderr.TD_OK

    def drop(self):
        """drop"""

        self.table.drop()
        return lib.tderr.TD_OK

