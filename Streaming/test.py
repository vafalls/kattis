#!/usr/bin/python

import time
import bisect
import operator
from pprint import pprint

# a = [(1,1),
#      (2,2),
#      (3,3),
#      (4,4),
#      (4,3),
#      (4,4),
#      (4,3),
#      (4,4),
#      (4,3),
#      (5,2),
#      (6,1)]
#
# print a
#
# i = 1
# while i < len(a):
#     if a[i][0]==a[i-1][0]:
#         a.insert(i+1,(a[i][0],a[i][1]+a[i-1][1]))
#         del a[i-1]
#         del a[i-1]
#     else:
#         i += 1
#
# print a

# print list(set(a))

a = [1,2,2,3]

print a[-1:2]

print bisect.bisect_left(a,2)