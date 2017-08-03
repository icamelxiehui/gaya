#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: stockhotmodule.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 三  6/28 14:50:39 2017
"""


import ConfigParser
import lib.loggingmodule
import lib.tderr
from stockhotindex import StockHotIndex

class StockHotModule:

    def __init__(self, config, log_module, mongo):
        """init"""

        self.config = config
        self.log_module = log_module
        self.mongo = mongo
        self.stock_hot_index = StockHotIndex(config, log_module, mongo)

    def process(self, input_data):
        """process"""
        self.log_module.info("query start process")

        rv = self.stock_hot_index.process(input_data)
        if lib.tderr.FAILED(rv):
            return rv

        input_data['response'] = {"data":"ok","error":1}
        return lib.tderr.TD_OK
