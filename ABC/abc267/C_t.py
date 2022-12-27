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

accumulate_A = [0]
for a in A:
    accumulate_A.append(accumulate_A[-1] + a)

v_tmp = 0
for i in range(m):
    v_tmp += A[i] * (i+1)
ans = v_tmp
for i in range(n-m):
    v_nxt = v_tmp - accumulate_A[m+i] + accumulate_A[i] + A[m+i] * m
    ans = max(ans, v_nxt)
    v_tmp = v_nxt
print(ans)
