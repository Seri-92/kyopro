from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**5)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

h, w = mi()
C = [li() for _ in range(h)]

dp = [[0] * w for _ in range(h)]

if C[h-1][w-1] == '.':
    dp[h-1][w-1] = 1

for i in range(h):
    for j in range(w):
        r, c = h-1-i, w-1-j
        if C[r][c] == '.':
            dp[r][c] = 1
        else:
            continue
        if r < h - 1:
            dp[r][c] = max(dp[r][c], dp[r+1][c] + 1)
        if c < w - 1:
            dp[r][c] = max(dp[r][c], dp[r][c+1] + 1)

print(dp[0][0])
