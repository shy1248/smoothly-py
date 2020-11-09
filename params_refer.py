#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 21:51:08
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 函数参数实例。
    Python中所有参数都是共享参数，即实参是形参的引用；
    Java中基本类型是值传递，其他类型也是引用传递；
    按照这种特性，可变参数在函数中被修改后会影响原来的值；
    因此不建议将可变参数作为函数参数的默认值，而应该使用None, 见幽灵巴士示例。
@ LastTime: 2019-07-28 22:13:32
'''


def func(a, b):
    # 此处必须用 += 这种就地修改操作， 使用 a = a + b 则无效
    a += b
    return a


if __name__ == "__main__":
    x, y = 1, 2
    print(x, y)
    func(x, y)
    print(x, y)

    l1, l2 = [10, 20], [30, 40]
    print(l1, l2)
    func(l1, l2)
    print(l1, l2)

    t1, t2 = (10, 20), (30, 40)
    print(t1, t2)
    func(t1, t2)
    print(t1, t2)

    # 幽灵巴士
    class HauntedBus(object):

        def __init__(self, passengers=[]):
            self.passengers = passengers

        def pick(self, person):
            self.passengers.append(person)

        def drop(self, person):
            self.passengers.remove(person)

    bus1 = HauntedBus(['Bill', 'Alice'])
    print(bus1.passengers)
    bus1.pick('Claire')
    bus1.drop('Alice')
    print(bus1.passengers)

    bus2 = HauntedBus()
    print(bus2.passengers)
    bus2.pick('claire')
    print(bus2.passengers)

    bus3 = HauntedBus()
    print(bus3.passengers)
    bus3.pick('Alice')
    print(bus3.passengers)
    # bus2和bus3具有相同的乘客
    print(bus1.passengers, bus2.passengers, bus3.passengers)
