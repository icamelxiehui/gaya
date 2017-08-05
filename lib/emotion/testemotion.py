#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: testemotion.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 六  8/ 5 19:02:23 2017
"""

import requests

query="上涨"
#query="下跌"
res = requests.post("http://127.0.0.1:5004",params={'query':query}).text
print res
