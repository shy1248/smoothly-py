#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-29 10:13:11
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 自定义类示例
@ LastTime: 2019-07-29 23:34:44
'''

import math
from array import array


class Vector2D(object):
    typecode = 'd'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        """pack and unpack"""
        return (_ for _ in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({}, {})'.format(class_name, *self)

    def __str__(self):
        # return str(tuple(self))
        return self.__repr__()

    # def __bytes__(self):
    #     # return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    #     return 'to bytes'

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # def __bool__(self):
    #     return bool(abs(self))


if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    print(v1)
    print(v1.x, v1.y)

    x, y = v1
    print(x, y)

    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)

    octets = bytes(v1)
    print(octets)

    print(abs(v1))

    print(bool(v1))

    print(bool(Vector2D(0, 0)))

    print(dir(v1))
