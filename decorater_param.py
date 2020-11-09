#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 20:34:26
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 带参数的装饰器
@ LastTime: 2019-07-28 20:49:24
'''

import time
from functools import wraps

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):

    def decorate(func):

        @wraps(func)
        def clocked(*_args, **_kwargs):
            start = time.time()
            _result = func(*_args, **_kwargs)
            elapsed = time.time() - start
            name = func.__name__
            arg_lst = []
            if _args:
                arg_lst.append(', '.join([repr(arg) for arg in _args]))
            if _kwargs:
                pairs = [
                    '{}={}'.format(repr(k), repr(v))
                    for k, v in _kwargs.items()
                ]
                arg_lst.append(', '.join(pairs))
            args = ', '.join(arg_lst)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate


if __name__ == "__main__":

    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    @clock(fmt='{name}: {elapsed}s')
    def snooze01(seconds):
        time.sleep(seconds)

    @clock('{name}({args}): {elapsed:0.3f}s')
    def snooze02(seconds):
        time.sleep(seconds)

    for _ in range(3):
        snooze(0.123)
        snooze01(0.123)
        snooze02(0.123)
