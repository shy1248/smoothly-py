#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 20:05:38
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 自带装饰器 singledispath 实例, 该装饰器可以实现类似于java中方法重载的效果
@ LastTime: 2019-07-28 20:24:09
'''

import numbers

from singledispatch import singledispatch


@singledispatch
def singled(obj):
    print('Calling singled <obj> using arg type: {} ...'.format(type(obj)))
    print(obj)


@singled.register(str)
def _(text):
    print('Calling singled <str> using arg type: {} ...'.format(type(text)))
    print(text)


@singled.register(numbers.Integral)
def _(number):
    print('Calling singled <numberic> using arg type: {} ...'.format(
        type(number)))
    print(number)


if __name__ == "__main__":
    singled('str')
    singled(10)
    singled(1.2)
    singled([])
