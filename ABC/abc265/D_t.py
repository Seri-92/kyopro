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

n, p, q, r = mi()
A = lmi()
accumulate_A = [0]
for i in range(n):
    accumulate_A.append(accumulate_A[-1] + A[i])

def f(s, v):
    top = n
    bottom = s
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if accumulate_A[mid] - accumulate_A[s] > v:
            top = mid
        else:
            bottom = mid
    if accumulate_A[bottom] - accumulate_A[s] == v:
        return bottom
    return False


for x in range(n):
    y = f(x, p)
    if not y:
        continue
    z = f(y, q)
    if not z:
        continue
    w = f(z, r)
    if not z:
        continue
    print('Yes')
    exit()

print('No')
