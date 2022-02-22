from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
# mod = 1000000007
mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n = ii()
len_n = len(str(n))
ans = 0
for i in range(len_n - 1):
    ans += (1 + 9 * 10 ** i) * 9 * 10 ** i // 2
    ans %= mod

m = n - (10 ** (len_n - 1) - 1)

ans += (1 + m) * m // 2
ans %= mod

print(ans)
