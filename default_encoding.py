#!/usr/bin/env python
# -*- coding=UTF-8 -*-
'''
@ Since: 2019-07-28 11:32:34
@ Author: shy
@ Email: yushuibo@ebupt.com / hengchen2005@gmail.com
@ Version: v1.0
@ Description: system default encoding demo
@ LastTime: 2019-07-28 11:40:20
'''

import io
import sys
import locale

expressions = """
    locale.getpreferredencoding()
    type(my_file)
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
"""

my_file = io.open('resources/dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print('{} => {}'.format(expression.rjust(30), repr(value)))
