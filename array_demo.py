#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-27 21:10:07
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: array demos
@ LastTime: 2019-07-27 21:45:59
'''

import random
from array import array

# 使用生成器长度为1000万创建一个存放双精度浮点型的数组
floats01 = array('d', (random.random() for _ in range(10**7)))
print(floats01[-1])
# 存入文件
with open('resources/floats.bin', 'wb') as f:
    floats01.tofile(f)

floats02 = array('d')

# 从文件读取
with open('resources/floats.bin', 'rb') as f:
    floats02.fromfile(f, 10**7)

print(floats02[-1])

print(floats01 == floats02)
