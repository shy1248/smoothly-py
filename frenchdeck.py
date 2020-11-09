#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-27 14:07:24
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: __getitem__
@ LastTime: 2019-07-27 15:56:42
'''

from __future__ import print_function

from collections import namedtuple
from random import choice

# nametuple 用于构建只有少数属性但是没有方法的对象，此处代表一张纸牌
Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.__cards = [
            Card(rank, suit) for rank in self.ranks for suit in self.suits
        ]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, index):
        return self.__cards[index]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    # 获取纸牌对象
    print(Card("7", "diamonds"))
    # 一幅扑克牌的总张数
    deck = FrenchDeck()
    print(len(deck))
    # 第一张
    print(deck[0])
    # 最后一张
    print(deck[-1])
    # 随机
    print(choice(deck))
    # 迭代
    for card in deck:
        print(card)
    # 排序
    for card in sorted(deck, key=spades_high):
        print(card)
