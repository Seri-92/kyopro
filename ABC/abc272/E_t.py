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
A = lmi()

exist_num_set = [set() for _ in range(m)]

for i in range(n):
    a = A[i]
    if a >= 0:
        cnt = 0
        a += i+1
    else:
        cnt = -(a // (i+1)) - 1
        a %= i+1
    idx = cnt
    while idx <= m-1 and a < n:
        exist_num_set[idx].add(a)
        a += i+1
        idx += 1

for i in range(m):
    for j in range(n):
        if j not in exist_num_set[i]:
            print(j)
            break
        if j == n - 1:
            print(n)

