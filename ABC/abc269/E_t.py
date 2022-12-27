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

n = ii()
r_bottom, r_top = 1, n
c_bottom, c_top = 1, n


while r_top - r_bottom > 0:
    r_mid = (r_bottom + r_top) // 2
    print('?', r_bottom, r_mid, 1, n)
    t = int(input())
    if t == r_mid - r_bottom:
        r_top = r_mid
    else:
        r_bottom = r_mid + 1



while c_top - c_bottom > 0:
    c_mid = (c_bottom + c_top) // 2
    print('?', 1, n, c_bottom, c_mid)
    t = int(input())
    if t == c_mid - c_bottom:
        c_top = c_mid
    else:
        c_bottom = c_mid + 1



print('!', r_bottom, c_bottom)

