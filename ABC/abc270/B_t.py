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

x, y, z = mi()

if 0 < y < x or x < y < 0:
    if 0 < y < z or z < y < 0:
        ans = -1
    else:
        ans = abs(z) + abs(x - z)

else:
    ans = abs(x)

print(ans)
