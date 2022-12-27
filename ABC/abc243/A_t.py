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

v, a, b, c = mi()


while True:
    v -= a
    if v < 0:
        print('F')
        exit()
    v -= b
    if v < 0:
        print('M')
        exit()
    v -= c
    if v < 0:
        print('T')
        exit()