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

x, a, d, n = mi()
if d == 0:
    ans = abs(x - a)
else:
    r = x % d

    if d > 0:
        if x <= a:
            ans = a - x
        elif x >= a + d * (n - 1):
            ans = x - (a + d * (n - 1))
        else:
            ans = min(abs(r - a % d), d - abs(r - a % d))
    else:
        if x >= a:
            ans = x - a
        elif x <= a + d * (n - 1):
            ans = a + d * (n - 1) - x
        else:
            ans = min(abs(r - a % d), -d - abs(r - a % d))

print(ans)
