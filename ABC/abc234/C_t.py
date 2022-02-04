from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())


k = ii()
ans = ''

for i in range(60, -1, -1):
    q, r = divmod(k, 2**i)
    k = r
    ans += str(q * 2)


print(int(ans))
