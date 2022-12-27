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

n, k = mi()
A = lmi()
B = lmi()

dp = [set() for _ in range(n)]
dp[0].add(A[0])
dp[0].add(B[0])

for i in range(1, n):
    a, b = A[i], B[i]
    for x in dp[i-1]:
        if abs(a - x) <= k:
            dp[i].add(a)
        if abs(b - x) <= k:
            dp[i].add(b)

if dp[-1]:
    print('Yes')
else: print('No')
