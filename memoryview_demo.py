#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-27 21:46:20
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: memoryview demos
@ LastTime: 2019-07-27 22:16:27
'''

import array

# 长度为5的段整型有符号整数数组
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
# memv_oct = memv.cast('B')
memv_oct = memv
memv_oct.tolist()
print(memv_oct)
memv_oct[5] = 4
print(numbers)
