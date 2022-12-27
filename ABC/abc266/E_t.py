from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))


def f(n):
    if n == 1:
        return 3.5
    ret = []
    x = f(n-1)
    for i in range(1, 7):
        ret.append(max(x, i))
    ret = sum(ret) / 6
    return ret

n = ii()
print(f(n))


