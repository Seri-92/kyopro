from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right

# sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n, k = mi()
a_list = lmi()
dict_ = defaultdict(int)
dict_[0] += 1

accumulate = 0
ans = 0
for i in range(n):
    accumulate += a_list[i]
    ans += dict_[accumulate - k] 
    dict_[accumulate] += 1

print(ans)

