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
t = input()
x = 0
y = 0

muki = 0
    
for i in range(n):
    if t[i] == 'R':
        muki += 1
        muki %= 4
    else:
        if muki == 0:
            x += 1
        elif muki == 1:
            y -= 1
        elif muki == 2:
            x -= 1
        else:
            y += 1

print(x, y)
