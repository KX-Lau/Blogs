"""
Name: test.py
Author: KX-Lau
Time: 2020/11/23 14:46
Desc: 
"""

import os
import sys
import my_module

print(__file__)

base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

print(my_module.name)
my_module.func()

# 一个模块能否被导入，就看这个模块所在的目录是否在sys.path中
# 正常的sys.path中除了内置、扩展模块外，只有一个路径永远不会出问题，那就是直接执行的文件所在的目录。

print(sys.path.append(r'F:\blogs\codes\glance'))
import my_module2
