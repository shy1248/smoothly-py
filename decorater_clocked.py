#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 18:56:36
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 真正意义上的第一个函数装饰器
@ LastTime: 2019-07-28 19:49:55
'''

import time


def clocked_first(func):

    def clocked(*args):
        start = time.time()
        res = func(*args)
        elapsed = time.time() - start
        name = func.__name__
        arg_str = ', '.join([str(arg) for arg in args])
        print('[{:0.8f}] {}{} -> {}'.format(elapsed, name, arg_str, res))
        return res

    return clocked


from functools import wraps


def std_clocked(func):
    # wraps的作用是复制func相关属性至clocked中，如__doc__, __name__等
    @wraps(func)
    def clocked(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        elapsed = time.time() - start
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [
                '{}={}'.format(repr(k), repr(v))
                for k, v in sorted(kwargs.items())
            ]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[{:0.8f}] {}{} -> {}'.format(elapsed, name, arg_str, res))
        return res

    return clocked
