#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 17:40:25
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 装饰器初步， 装饰器会修改被装饰的函数的行为
@ LastTime: 2019-07-28 17:46:25
'''


def deco(func):

    def inner():
        print('Runnning inner func...')

    return inner


# 此处等价于： target = deco(target)
# 实际上是将变量tartget重新指向了deco函数返回的函数
@deco
def target():
    print('Running target func...')


if __name__ == "__main__":
    target()
