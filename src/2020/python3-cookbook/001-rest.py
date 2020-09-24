#!/usr/bin/python3
#-- coding:utf8 --

# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p01_unpack_sequence_into_separate_variables.html

p = (4, 5)
x, y = p
print(x, y)
print('=====')

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

name, shares, price, (year, mon, day) = data

print(name)
print(shares)
print(price)
print(year)
print(mon)
print(day)
# python3 src/2020/python3-cookbook/001-rest.py
