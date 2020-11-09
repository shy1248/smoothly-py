#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 18:56:36
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 真正意义上的第一个函数装饰器
@ LastTime: 2019-07-28 19:47:44
'''
import time

from decorater_clocked import clocked_first
from decorater_clocked import std_clocked


@std_clocked
# @clocked_first
def snooze(seconds):
    time.sleep(seconds)


@std_clocked
# @clocked_first
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial.__name__)
    print('*' * 40, 'Calling snooze(0.123) ...')
    snooze(0.123)
    print('*' * 40, 'Calling factorial(6)...')
    res = factorial(6)
    print('6! = {}'.format(res))
