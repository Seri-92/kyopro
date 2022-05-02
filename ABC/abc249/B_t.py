from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

s = ls()
n = len(s)
set_ = set()
large = False
small = False
for c in s:
    if ord(c) <= 90:
        large = True
    if ord(c) >= 97:
        small = True
    set_.add(ord(c))
if len(set_) == n and large and small:
    print('Yes')
else:
    print('No')
