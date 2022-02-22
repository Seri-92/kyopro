from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

s = ls()
s = [0] + s
l = len(s)

t = '0chokudai'

dp = [[0] * 9 for _ in range(l)]


for i in range(l):
    for j in range(9):
        if j == 0:
            dp[i][j] = 1
        else:
            if i > 0:
                if s[i] == t[j]:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
                else:
                    dp[i][j] = dp[i-1][j]

print(dp[l-1][8])
