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
B = lmi()

A_max = max(A)

eat_num = set()
for i in range(n):
    if A[i] == A_max:
        eat_num.add(i)

for i in range(k):
    if B[i] - 1 in eat_num:
        print('Yes')
        exit()

print('No')
