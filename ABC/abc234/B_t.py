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

n = ii()
list_ = []
for _ in range(n):
    list_.append(lmi())

ans = 0
for i in range(n):
    for j in range(n):
        a, b = list_[i]
        c, d = list_[j]

        ans = max(ans, (a-c)**2 + (b-d)**2)

print(math.sqrt(ans))
