#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 15:19:09
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 策略模式，模拟Java语言实现
@ LastTime: 2019-07-28 16:22:39
'''

from abc import ABCMeta
from abc import abstractmethod
from collections import namedtuple

# 命名元组，表示一个顾客名字和他的积分
Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):
    """单品类"""

    def __init__(self, product_name, quantity, unit_price):
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def total(self):
        return self.quantity * self.unit_price


class Order(object):
    """订单类"""

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if not self.promotion:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        fmt = '<Order[total: {:.2f} due: {:.2f}]>'
        return fmt.format(self.total(), self.due())


class Promotion():
    """折扣策略类，抽象接口"""

    __meta__ = ABCMeta

    def discount(self, order):
        """返回折扣金额（正值）"""
        pass


class FidetityPromotion(Promotion):
    """积分折扣策略实现：大于1000积分的顾客提供5%的折扣"""

    def discount(self, order):
        return order.total() * 0.5 if order.customer.fidelity > 1000 else 0


class BulkItemPromotion(Promotion):
    """单品大客户折扣实现：单品超过20的顾客提供10%的折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity > 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromotion(Promotion):
    """大订单折扣实现: 订单中不同商品数大于10时提供7%的折扣"""

    def discount(self, order):
        distinct_item = {item.product_name for item in order.cart}
        if len(distinct_item) > 10:
            return order.total() * 0.7
        return 0


if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart01 = [
        LineItem('Banana', 4, 0.5),
        LineItem('Apple', 10, 1.5),
        LineItem('Watermellon', 5, 5.0)
    ]

    cart02 = [LineItem('Banana', 24, 0.5), LineItem('Apple', 10, 1.5)]

    cart03 = [LineItem(item_code, 1, 1.0) for item_code in range(20)]

    print('Customer: {} ==> {}'.format(
        joe, Order(joe, cart01, promotion=FidetityPromotion())))

    print('Customer: {} ==> {}'.format(
        ann, Order(ann, cart01, promotion=FidetityPromotion())))

    print('Customer: {} ==> {}'.format(
        joe, Order(joe, cart02, promotion=BulkItemPromotion())))

    print('Customer: {} ==> {}'.format(
        joe, Order(joe, cart03, promotion=LargeOrderPromotion())))
