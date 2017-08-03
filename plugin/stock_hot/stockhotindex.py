#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: stockhotindex.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 三  6/28 14:52:49 2017
"""
import ConfigParser
import lib.loggingmodule
import lib.tderr

class StockHotIndex:

    def __init__(self, config, log_module, mongo):
        """init"""

        self.config = config
        self.log_module = log_module
        self.mongo = mongo

    def get_hot_index(self):
        """get_hot_index"""

        self.mongo.seting("big_data", "sogou_index")
        self.stock_index_list = []
        for item in self.mongo.find_all():
            self.stock_index_list.append(item)
        
        return lib.tderr.TD_OK

    def merge(self, code, stock_trade, stock_index):
        """merge"""

        self.mongo.seting("big_data_final", "stock_qfq_index")

        max_index = -1
        tmp_dict = {}
        for item in stock_index:
            tmp_dict[item["date"]] = item["whole_index"]
            if item["whole_index"] > max_index:
                max_index = item["whole_index"]

        max_price = -1
        for item in stock_trade:
            if item["high"] > max_price:
                max_price = item["high"]

        result = {'code':code, 'data':[]}
        for item in stock_trade:
            tmp = {'qfq_price':{},'date':item['date']}
            tmp['qfq_price']['open'] = item['open']
            tmp['qfq_price']['close'] = item['close']
            tmp['qfq_price']['low'] = item['low']
            tmp['qfq_price']['high'] = item['high']

            if tmp_dict.has_key(item["date"]):
                tmp["whole_index"] = int(tmp_dict[item["date"]]) * max_price / max_index
            else:
                tmp["whole_index"] = 0
            result["data"].append(tmp)
        self.mongo.save(result)
	



    def process(self, input_data):
        """process"""

        self.get_hot_index()
        
        for item in self.stock_index_list:
            code = item['code']
            code = "300467"
            self.mongo.seting("big_data", "stock_trade")
            stock_trade = self.mongo.find_one({'code':code})
            self.merge(item['code'], stock_trade['qfq_data'], item['data'])

        return lib.tderr.TD_OK
