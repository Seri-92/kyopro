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

d = defaultdict(int)
for i in range(1, 10):
    d[i] = 1

for i in range(n-1):
    d_tmp = defaultdict(int)
    for j in range(1, 10):
        if j - 1 >= 1:
            d_tmp[j-1] += d[j]
        d_tmp[j] += d[j]
        if j + 1 <= 9:
            d_tmp[j+1] += d[j]

    for j in range(1, 10):
        d[j] = d_tmp[j] % mod 

ans = 0
for i in range(1, 10):
    ans += d[i]
        

ans %= mod
print(ans)
    
