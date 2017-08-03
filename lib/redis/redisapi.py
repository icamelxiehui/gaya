#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-05-27 15:13:22
@author xiehui
"""

import redis
import os
class RedisApi(object):
    """Class wrap redis"""
    def __init__(self, config):
        self.config = config
        self.bns_name = self.config.get("redis", "feed_back_redis_bns")
        self.redis_handler = self.getRedisHandler()
        
    def getRedisHandler(self):
        """get redis by ip and port"""
        (redis_ip, redis_port) = self.parserBns()
        return self.getHandlerByIp(redis_ip, redis_port)

    def getHandlerByIp(self, redis_ip, redis_port):
        """sub function to getRedisHandle"""
        pool = redis.ConnectionPool(host=redis_ip, port=redis_port, db=0)
        return redis.StrictRedis(connection_pool = pool)

    def parserBns(self):
        """get server ip and port form bns"""
        cmd = "get_instance_by_service -arm " + self.bns_name + " | cut -d' ' -f2,4 | head -n 1"
        res = os.popen(cmd)
        return res.read().strip().split()
       
    def findall(self, key_list):
        """find all item in redis"""
        for i in range(3):
            try:
                return self.redis_handler.mget(key_list) 
            except:
                continue
    def find(self, key):
        """find a item in redis"""
        return self.redis_handler.get(key)

    def set(self, key, value):
        """set a item in redis"""
        return self.redis_handler.set(key, value) 

    def delete(self, key):
        """delete a item from redis"""
        return self.redis_handler.delete(key)
    
#if __name__ == "__main__":
    #ra = RedisApi('')
    #ra.parserBns('')
