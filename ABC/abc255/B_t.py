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

n, k = mi()
A = lmi()
for i in range(k):
    A[i] -= 1
A_set = set(A)
position_list = []
for _ in range(n):
    position_list.append(lmi())

dist_max = 0
for b in range(n):
    dist = 1e7
    if b in A_set:
        continue
    for a_r in A:
        a_r_x, a_r_y = position_list[a_r]
        b_x, b_y = position_list[b]
        dist_tmp = math.sqrt((a_r_x - b_x) ** 2 + (a_r_y - b_y) ** 2)
        dist = min(dist_tmp, dist)
    dist_max = max(dist, dist_max)

print(dist_max)
