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
P = lmi()

field = []
d = defaultdict(int)

def bs(field, p, i):
    if not field:
        field.append(deque([p]))
        return field
    ok = len(field) - 1
    if field[ok][0] < p:
        field[ok].append(deque([p]))
        if len(field[ok]) == k:
            eaten = field.pop(ok)
            for x in eaten:
                print(type(x))
                d[x] = i
        return field
    ng = 0
    if field[ng][0] > p:
        field[ng].appendleft(p) 
        if len(field[ng]) == k:
            eaten = filed.pop(ng)
            for x in eaten:
                d[x] = i
        return field

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if field[mid][0] < p:
            ng = mid
        else:
            ok = mid
    field[ok].appendleft(p)
    if len(field[ok]) == k:
        eaten = field.pop(ok)
        for x in eaten:
            d[x] = i
    return field


for i in range(n):
    p = P[i]
    field = bs(field, p, i+1)

print(d)

    



