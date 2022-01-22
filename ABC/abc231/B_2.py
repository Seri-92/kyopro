from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

n = ii()
dict_ = {}
for i in range(n):
    s = input()
    if s in dict_:
        dict_[s] += 1
    else:
        dict_[s] = 1

ans = max(dict_, key = dict_.get)
print(ans)
