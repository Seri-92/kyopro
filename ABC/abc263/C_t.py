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

n, m = mi()

ans_list = []

for i in range(1<<m):
    l = []
    for j in range(m):
        if i >> j & 1 == 1:
            l.append(j+1)
    if len(l) == n:
        ans_list.append(l)

ans_list.sort()
for ll in ans_list:
    print(*ll)

