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

n, m, t = mi()
A = lmi()
bonus = [0] * n
for _ in range(m):
    x, y = mi()
    bonus[x-1] = y

# print(bonus)
cnt = 0
for i in range(n-1):
    a = A[i]
    if t > a:
        t -= a
        t += bonus[i+1]
    else:
        print('No')
        exit()

print('Yes')
