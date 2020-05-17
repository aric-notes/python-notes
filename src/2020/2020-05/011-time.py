#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

ticks = time.time()
print "当前时间戳为:", ticks


# localtime = time.localtime(time.time())
# print "本地时间为 :", localtime


# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
