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

n, s = mi()
cards = [0] + [lmi() for _ in range(n)]

dp = [[[] for _ in range(s+300)] for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(s):
        a, b = cards[i+1]
        if dp[i][j]:
            dp[i+1][j+a].append([a, 'H'])
            dp[i+1][j+b].append([b, 'T'])

if not dp[n][s]:
    print('No')
    exit()
else:
    ans = ''
    while s:
        ans += dp[n][s][0][1]
        x = dp[n][s][0][0] 
        n -= 1
        s -= x
print('Yes')     
print(ans[::-1])
    
