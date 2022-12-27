from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

#0x9CC sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))


n, l = map(int, input().split())
abs_min = 1000
all_sum = 0
for i in range(n):
    if abs(l+i) < abs(abs_min):
        abs_min = l+i
    all_sum += l+i

print(all_sum - abs_min)

