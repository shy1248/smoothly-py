#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 21:24:31
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 对象的浅复制与深复制实例。
    浅复制：只复制最外部的容器，内部只是引用，及内部数据是同一份，对于这些内部数据中可变对象的改变，会影响到复制后的对象；
    而对于不可变对象的改变，则会改变这种应用关系，重新创建新的；
    深复制：从内到外都是重新创建的，改变原来的不影响复制品；
    一般通过构造函数和[:]操作的复制都是浅复制；深复制需要copy模块中的deepcopy方法实现
@ LastTime: 2019-07-28 22:14:06
'''

import copy


class Bus(object):

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, person):
        self.passengers.append(person)

    def drop(self, person):
        self.passengers.remove(person)


if __name__ == "__main__":
    bus = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus_cp = copy.copy(bus)
    bus_dcp = copy.deepcopy(bus)

    print(id(bus), id(bus_cp), id(bus_dcp))
    bus_cp.drop('Bill')
    print(bus.passengers)
    print(bus_cp.passengers)
    print(bus_dcp.passengers)
    print(id(bus.passengers), id(bus_cp.passengers), id(bus_dcp.passengers))
