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

n = int(input())
l = [[] for _ in range(10**5+10)]
l = [0] * (10**5+10)
for i in range(n):
    t, x, a = map(int, input().split())
    l[t] = (x, a)

dp = [[-1] * (5) for _ in range(10**5+10)]
dp[0][0] = 0


for t in range(10**5+8):
    for i in range(5):
        dp[t+1][i] = max(dp[t+1][i], dp[t][i])
        if i > 0:
            dp[t+1][i-1] = max(dp[t+1][i-1], dp[t][i])
        if i < 4:
            dp[t+1][i+1] = max(dp[t+1][i+1], dp[t][i])
            
        if l[t+1]:
            x, a = l[t+1]
            if abs(x - i) < 2 and dp[t][i] >= 0:
                dp[t+1][x] = max(dp[t][i] + a, dp[t+1][x])
print(max(dp[10**5][i] for i in range(5)))
            



