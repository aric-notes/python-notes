#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Site:
  # 注意，这里如果是 __url__ 情况又不一样了。
  __url= 'www.baidu.com'

  def print_me(self):
    print(self.__url)


site = Site()
site.print_me()

print(site._Site__url)
