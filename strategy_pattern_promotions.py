#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 17:03:04
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: 所有的折扣策略放入此模块，然后使用inspect模块内省获取策略函数，共best_promotion方法选择
@ LastTime: 2019-07-28 17:04:43
'''


def fidetity_promotion(order):
    """积分折扣策略实现：大于1000积分的顾客提供5%的折扣"""
    return order.total() * 0.5 if order.customer.fidelity > 1000 else 0


def bulkitem_promotion(order):
    """单品大客户折扣实现：单品超过20的顾客提供10%的折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity > 20:
            discount += item.total() * 0.1
    return discount


def largeorder_promotion(order):
    """大订单折扣实现: 订单中不同商品数大于10时提供7%的折扣"""
    distinct_item = {item.product_name for item in order.cart}
    if len(distinct_item) > 10:
        return order.total() * 0.7
    return 0
