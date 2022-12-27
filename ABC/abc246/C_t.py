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

n, k, x = mi()
A = lmi()
A.sort(reverse=True)

for i in range(n):
    q, r = divmod(A[i], x)
    if k >= q:
        A[i] = r
        k -= q
    else:
        A[i] -= k * x
        k = 0
        break

A.sort(reverse=True)
for i in range(n):
    if k > 0:
        k -= 1
        # A[i] = max(0, A[i]-x)
        A[i] = 0


print(sum(A))

    
