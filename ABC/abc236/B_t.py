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
A = lmi()

dict_ = defaultdict(int)
for i in range(4 * n - 1):
    x = A[i]
    dict_[x] += 1

for i in range(1, n+1):
    if dict_[i] != 4:
        print(i)
        exit()
