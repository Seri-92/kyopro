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

n = ii()
P = lmi()

point_list = [0] * n

for i in range(n):
    p = P[i]
    dist = (i - p) % n
    point_list[dist] += 1
    point_list[(dist-1) % n] += 1
    point_list[(dist+1) % n] += 1

print(max(point_list))



