#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 18:25:44
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 闭包示例
@ LastTime: 2019-07-28 18:50:41
'''

from __future__ import division


class Avrager(object):
    """计算历史平均值，类实现"""

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)


def make_avrager():
    """计算历史平均值，闭包实现"""

    series = []

    def avrager(new_value):
        # 函数返回后，该变量成为自由变量（free variable），即未在本地作用域绑定的变量
        series.append(new_value)
        return sum(series) / len(series)

    return avrager


def make_avrager_op():
    """计算历史平均值，闭包实现，优化list形式，只保留上一次计算的和数量"""

    # total = 0
    # count = 0
    last = {'t': 0, 'c': 0}

    def avrager(new_value):
        # 此种方式存在的问题是，在函数中尝试对自由变量重新绑定，会将自由变量变成局部变量
        # 在上面的方法中，并没有对自由变量series重新绑定，而是利用了list的可变属性
        # 在python3中可以使用nonlocal关键字，如下，将本地变量声明为自由变量
        # nonlocal total, count
        # count += 1
        # total += new_value
        # return total / count

        # python2中没有nonlocal关键字，因此需要将局部变量存储为可变对象
        last['t'] = last['t'] + new_value
        last['c'] = last['c'] + 1
        return last['t'] / last['c']

    return avrager


if __name__ == "__main__":
    cls_avg = Avrager()
    func_avg = make_avrager()
    func_avg_op = make_avrager_op()

    print(cls_avg(10))
    print(cls_avg(11))
    print(cls_avg(12))
    print(cls_avg(13))

    print(func_avg(10))
    print(func_avg(11))
    print(func_avg(12))
    print(func_avg(13))

    print(func_avg_op(10))
    print(func_avg_op(11))
    print(func_avg_op(12))
    print(func_avg_op(13))
