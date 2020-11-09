#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 12:45:19
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: __call__ demo, 覆盖了__call__方法的类实例可以直接被调用
@ LastTime: 2019-07-28 15:09:14
'''

import random


class BingoCage(object):

    def __init__(self, items):
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage.')

    def __call__(self):
        return self.pick()


if __name__ == "__main__":
    bingo = BingoCage(range(10))
    print(bingo.pick())
    print(callable(bingo))
    # 覆盖了__call__方法的类实例可以直接被调用
    print(bingo())
