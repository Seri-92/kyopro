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

def ccw(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    bx -= ax
    by -= ay
    cx -= ax
    cy -= ay

    return bx * cy - by * cx > 0

V = [lmi() for _ in range(4)]

for i in range(4):
    if not ccw(V[i], V[(i+1)%4], V[(i+2)%4]):
        print('No')
        exit()

print('Yes')
