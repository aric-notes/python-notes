import os


# output = os.system("ls -alh")
output2 = os.popen('ls -alh', 'r')


# print(output)
print(output2.read())
# python3 src/2020/2020-09/001-system.py
# 0
