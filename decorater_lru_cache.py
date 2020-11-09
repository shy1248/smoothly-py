#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 19:51:19
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 自带装饰器 functools.lru_cache实现了备忘录模式
@ LastTime: 2019-07-28 19:59:16
'''

from backports.functools_lru_cache import lru_cache

from decorater_clocked import std_clocked


@lru_cache()
@std_clocked
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(6))
