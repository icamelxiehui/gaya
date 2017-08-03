#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-05-30 16:55:23
@author xiehui
"""

TD_OK=                    0
TD_ERROR_FAILTRUE=       -1
TD_ERROR_ABORT=          -2  #仅为了终端流程
TD_ERROR_UNEXPECTED=     -3
TD_ERROR_BAD_PARAMETER=  -4

TD_ERROR_RETRY=          -5


def SUCCESS(code):
    """input equal to TD_OK"""
    return code == TD_OK


def FAILED(code):
    """input not equal to TD_OK"""
    return code != TD_OK



