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
X = [0] + lmi()
dp = [[0] * (n+1) for _ in range(n+1)]
bonus_dict = defaultdict(int)
for i in range(m):
    c, y = lmi()
    bonus_dict[c] = y

for i in range(n):
    for j in range(1, n+1):
        if j > i + 1:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + X[i+1] + bonus_dict[j])
    dp[i+1][0] = max(dp[i])

print(max(dp[-1]))
