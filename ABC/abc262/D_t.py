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

n = ii()
A = lmi()

ans = 0
for i in range(1, n+1):
    # i は使う個数
    dp = [[[0] * i for _ in range(n+1)] for _ in range(n+1)]
    dp[1][1][A[0] % i] += 1
    dp[1][0][0] += 1
    for j in range(2, n+1):
        for k in range(i+1):
            for l in range(i):
                if k >= 1:
                    dp[j][k][l] += dp[j-1][k-1][(l - A[j-1]) % i]
                dp[j][k][l] += dp[j-1][k][l]
    ans += dp[-1][i][0]
    ans %= mod

print(ans)
    



