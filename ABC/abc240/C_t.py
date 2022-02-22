from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
# mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n, x = mi()
list_ = [0] + [lmi() for _ in range(n)]
dp = [[0] * (x+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(x+1):
        a, b = list_[i]
        if j-a >= 0:
            if dp[i-1][j-a]:
                dp[i][j] = 1
        if j-b >= 0:
            if dp[i-1][j-b]:
                dp[i][j] = 1

        
print('Yes' if dp[n][x] else 'No')
