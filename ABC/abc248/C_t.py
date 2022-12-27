from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# sys.setrecursionlimit(10**7)
# mod = 1000000007
mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n, m, k = mi()
# dp[i][j] := 長さiで総和がj以下の個数

dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(k+1):
        for t in range(1, m+1):
            if j - t < 0:
                continue
            dp[i+1][j] += dp[i][j-t]
            dp[i+1][j] %= mod

print(sum(dp[n]) % mod)

