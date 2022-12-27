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

dp = [0] * (n+1)

for i in range(n+1):
    for j in range(k):
        if A[j] <= i:
            dp[i] = max(dp[i], A[j] + (i - A[j] - dp[i - A[j]]))

        
print(dp[n])


