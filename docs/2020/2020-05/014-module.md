# modules
> https://www.runoob.com/python/python-modules.html


- Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
- 模块让你能够有逻辑地组织你的 Python 代码段。
- 把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
- 模块能定义函数，类和变量，模块里也能包含可执行的代码。

## load multiple times
- 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

## from…import 语句
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：

from modname import name1[, name2[, ... nameN]]
例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：

from fib import fibonacci
这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。


