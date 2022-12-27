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

attendance_list = list()

for _ in range(m):
    L = lmi()
    k = L[0]
    attendance = set(L[1:])
    attendance_list.append(attendance)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        flag = False
        for k in range(m):
            if i in attendance_list[k] and j in attendance_list[k]:
                flag = True
        if not flag:
            print('No')
            exit()

print('Yes')

