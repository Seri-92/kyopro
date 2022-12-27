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

group_list = [[] for _ in range(k)]
for i in range(n):
    group_num = i % k
    group_list[group_num].append(A[i])


for i in range(k):
    group_list[i].sort(reverse=True)

B = []
cnt = 0
for i in range(n):
    x = group_list[i % k].pop()
    B.append(x)


A.sort()

if A == B:
    print('Yes')
else:
    print('No')
