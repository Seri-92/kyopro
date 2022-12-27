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

n, a, m, k = map(int, input().split())

if m > k * n:
    top = a * n
    bottom = 0
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if m / (n + mid) >= k:
            top = mid
        else:
            bottom = mid
            
    print(top)

else:
    top = a * n
    bottom = 0
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if (m + a) // (n + mid) <= k:
            bottom = mid
        else:
            top = mid
    print(bottom)
