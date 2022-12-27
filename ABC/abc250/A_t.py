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

h, w = mi()
r, c = mi()

cnt = 0
for dr in (-1, 0, 1):
    for dc in (-1, 0, 1):
        if abs(dr) + abs(dc) == 1:
            if 1 <= r + dr <= h and 1 <= c + dc <= w:
                cnt += 1
print(cnt)
