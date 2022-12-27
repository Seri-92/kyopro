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

n, m = mi()
A = [0] + lmi()

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    x = min(m, i)
    for j in range(1, x+1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + A[i] * j
        else:
            dp[i][j] = max(dp[i-1][j-1] + A[i] * j, dp[i-1][j])

print(dp[n][m])

