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
A = lmi()


A_sorted = sorted(A)[::-1]
dict_ = {}
cnt = 0
for a in A_sorted:
    if a not in dict_:
        dict_[a] = cnt
        cnt += 1

ans_list = [0] * n
for i in range(n):
    a = A[i]
    ans_list[dict_[a]] += 1

for ans in ans_list:
    print(ans)
