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

n, k = mi()
P = lmi()

list_ = P[:k]
list_.sort()
print(list_[0])

for i in range(k, n):
    x = P[i]
    heappush(list_, x)
    heappop(list_)
    print(list_[0])


