#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: test.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 四  8/ 3 15:52:51 2017
"""
for line in file("finance_negative.dat").readlines():
    for item in line.split("，"):
        if item.strip():
            print item
