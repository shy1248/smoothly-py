#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 13:23:36
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: Bobo 是一个HTTP微框架， bobo.exe -f bobo_demo.py
@ LastTime: 2019-07-28 14:48:03
'''

import bobo


@bobo.query('/')
def hello(persion):
    return ('Hello, {}'.format(persion))
