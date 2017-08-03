#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time-stamp: <2014-10-11 18:29:38 Saturday by nilin>
"""
################################################################################
#                                  _ooOoo_
#                                 o8888888o
#                                 88" . "88
#                                 (| -_- |)
#                                 O\  =  /O
#                              ____/`---'\____
#                            .'  \\|     |//  `.
#                           /  \\|||  Z  |||//  \
#                          /  _||||| -G- |||||-  \
#                          |   | \\\  H  /// |   |
#                          | \_|  ''\---/''  |   |
#                          \  .-\__  `-`  ___/-. /
#                        ___`. .'  /--.--\  `. . __
#                     ."" '<  `.___\_<|>_/___.'  >'"".
#                    | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#                    \  \ `-.   \_ __\ /__ _/   .-` /  /
#               ======`-.____`-.___\_____/___.-`____.-'======
#                                  `=---='
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                        佛祖保佑       永无BUG
#                        只加工资       不改需求
###############################################################################

import os
import logging
import logging.handlers


class LoggingModule(object):
    """
    将log模块进行了封装，方便调用，其中警告和错误会单独打印到wf文件，所有日志会打印到.log文件
    """
    def __init__(self):
        self.logger = logging.getLogger()

        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical

    def init_log(self, log_path, level=logging.INFO, when="D", backup=7,
                 format="%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d \
                         * %(thread)d %(message)s",
                 datefmt="%m-%d %H:%M:%S"):
        """
        init_log - initialize log module

        Args:
        log_path      - Log file path prefix.
                        Log data will go to two files: log_path.log and log_path.log.wf
                        Any non-exist parent directories will be created automatically
        level         - msg above the level will be displayed
                        DEBUG < INFO < WARNING < ERROR < CRITICAL
                       the default value is logging.INFO
        when          - how to split the log file by time interval
                        'S' : Seconds
                        'M' : Minutes
                        'H' : Hours
                        'D' : Days
                        'W' : Week day
                        default value: 'D'
        format        - format of the log
                        default format:
                        %(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s
                        INFO: 12-09 18:02:42: logging_module.py:40 * 139814749787872 HELLO WORLD
        backup        - how many backup file to keep
                        default value: 7

        Raises:
            OSError: fail to create log directories
            IOError: fail to open log file
        """
        formatter = logging.Formatter(format, datefmt)

        self.logger.setLevel(level)

        dir = os.path.dirname(log_path)
        if not os.path.isdir(dir):
            os.makedirs(dir)

        handler = logging.handlers.TimedRotatingFileHandler(log_path + ".log",
                                                            when=when,
                                                            backupCount=backup)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        handler = logging.handlers.TimedRotatingFileHandler(log_path + ".log.wf",
                                                            when=when,
                                                            backupCount=backup)
        handler.setLevel(logging.WARNING)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


