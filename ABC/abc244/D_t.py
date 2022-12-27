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

s = list(input().split())
t = list(input().split())
d = dict()
for i in range(3):
    d[s[i]] = i

l = []
for i in range(3):
    l.append(d[t[i]])

tento = 0
for i in range(3):
    for j in range(i, 3):
        if l[i] > l[j]:
            tento += 1
if tento % 2 == 0:
    print('Yes')
else:
    print('No')
