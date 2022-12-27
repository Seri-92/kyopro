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

dp = [[0] * m for _ in range(n)]
for j in range(m):
    dp[0][j] = 1

for i in range(n-1):
    accumulate_list = [0]
    for j in range(m):
        accumulate_list.append((accumulate_list[-1] + dp[i][j]) % mod)
    # accumulate_list = [0] + list(accumulate(dp[i]))
    for j in range(m):
        if k == 0:
            dp[i+1][j] = accumulate_list[m] % mod
        else:
            dp[i+1][j] = (accumulate_list[m] - accumulate_list[min(m, j+k)] + accumulate_list[max(0, j-k+1)]) % mod

ans = 0
for j in range(m):
    ans += dp[n-1][j]
    ans %= mod

print(ans)
