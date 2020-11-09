#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 22:37:03
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 弱引用示例。
    弱引用不会增减被引用对象的引用计数;
    Python中基础类型的list，tuple， int等不能作为弱引用所指对象；
    但是set可以；
    自定义的继承自list的对象也可以；
@ LastTime: 2019-07-30 13:49:14
'''

from weakref import WeakValueDictionary


class Cheese(object):

    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Cheese[{}]'.format(self.kind)


if __name__ == "__main__":
    # WeadkValueDictionary 常用于做缓存
    # 类似的还有 WeakKeyDictionary 和 WeakSet
    stock = WeakValueDictionary()
    catalog = [
        Cheese('Red Leicester'),
        Cheese('Tilsit'),
        Cheese('Brie'),
        Cheese('Parmesan')
    ]

    for cheese in catalog:
        stock[cheese.kind] = cheese

    print(stock.keys())
    del catalog
    print(stock.keys())
    # cheese 是全局变量，因此 Parmesan Cheese比其他奶酪存活时间久，必须显示的删除cheese引用，才会使所有奶酪消失
    del cheese
    print(stock.keys())
