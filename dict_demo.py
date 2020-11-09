#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-27 22:43:24
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: dict demo
@ LastTime: 2019-07-27 23:30:30
'''

import re
import sys
import collections

WORD_PATTERN = re.compile(r'\w+')

# 使用默认字典
# index = {}
index = collections.defaultdict(list)

with open(sys.argv[1], 'r') as fp:
    for row_no, line in enumerate(fp, start=1):
        for match in WORD_PATTERN.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            # 修改key的值

            # 不推荐的做法
            # current_loc = index.get(word, [])
            # current_loc.append((row_no, column_no))
            # index[word] = current_loc
            # 推荐做法
            # setdefault，key不存在返回设置的默认值，否则返回key对应的value
            # 通过此方法可以减少对字典的访问次数
            # index.setdefault(word, []).append((row_no, column_no))
            # 使用defaultdict形式
            index[word].append((row_no, column_no))

for word in sorted(index, key=str.upper):
    print('{} --> {}'.format(word, index[word]))


# 自定义dict类，覆盖__missing__方法为key提供默认值
class StrKeyedDict(dict):

    # __missing__方法只在—__getitem__方法中被调用，因此 d[k] 这种操作会调用到
    # 但是对于 get() 或者 k in d 这种操作不会有影响
    def __missing__(self, key):
        # 此处必须做类型检测这一步，否则当key不存在时会导致无限递归调用__missing__
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        # 此处如果用 key in self，会导致无限递归调用__contains__
        return key in self.keys() or str(key) in self.keys()
