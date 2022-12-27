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
interval_list = [lmi() for _ in range(n)]

interval_union = [0] * 10**6

for x, y in interval_list:
    interval_union[x] += 1
    interval_union[y] -= 1

l = list(accumulate(interval_union))

start = 0

flag = False
for i in range(len(l)):
    if flag:
        if l[i] == 0:
            flag = False
            print(start, i)
    else:
        if l[i] > 0:
            flag = True
            start = i
