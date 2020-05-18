#!/usr/bin/python
# -*- coding: UTF-8 -*-

def hello():
  print "hello world"


def argxxx(*args):
  print args

res = hello()
print res


argxxx(10)
argxxx(10,20)
argxxx(10, 20, 30)
