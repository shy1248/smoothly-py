#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 15:19:09
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 策略模式，使用Python函数实现，拓展自动选择最佳策略
@ LastTime: 2019-07-28 17:08:04
'''

import inspect
from collections import namedtuple

import strategy_pattern_promotions

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
            discount = self.promotion(self)

        return self.total() - discount

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        fmt = '<Order[total: {:.2f} due: {:.2f}]>'
        return fmt.format(self.total(), self.due())


def best_promotion(order):
    """所有的折扣策略中选择最大的折扣策略"""
    # 使用inspect模块内省独立的策略模块来获取所有的策略函数
    all_promotions = [
        func for _, func in inspect.getmembers(strategy_pattern_promotions,
                                               inspect.isfunction)
    ]
    return max(promotion(order) for promotion in all_promotions)


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
        joe, Order(joe, cart01, promotion=best_promotion)))

    print('Customer: {} ==> {}'.format(
        ann, Order(ann, cart01, promotion=best_promotion)))

    print('Customer: {} ==> {}'.format(
        joe, Order(joe, cart02, promotion=best_promotion)))

    print('Customer: {} ==> {}'.format(
        joe, Order(joe, cart03, promotion=best_promotion)))
