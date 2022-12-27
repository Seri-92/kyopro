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

n = bin(ii())
l = len(n) - 2
list_ = []
for i in range(l):
    if n[-i-1] == '1':
        list_.append(i)

l2 = len(list_)

for x in range(1<<l2):
    t = 0
    for i in range(l2):
        if x >> i & 1:
            t += 2 ** list_[i]
    print(t)

