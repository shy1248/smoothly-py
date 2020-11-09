#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 17:48:10
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 装饰器在他们装饰的函数被定义后立即执行，这通常是导入时（即python加载模块时）
@ LastTime: 2019-07-28 17:54:54
'''

registries = []


def register(func):
    print('Running register ({})...'.format(func))
    registries.append(func)
    return func


@register
def f1():
    print('Running f1...')


@register
def f2():
    print('Running f2...')


def f3():
    print('Running f3...')


def main():
    print('Running main...')
    print('registries ==> {}'.format(registries))
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
