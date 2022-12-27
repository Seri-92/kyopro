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

h, w = mi()
board = []
zahyo = []
for i in range(h):
    s = ls()
    for j in range(w):
        if s[j] == 'o':
            zahyo.append((i, j))

print(abs(zahyo[0][0] - zahyo[1][0]) + abs(zahyo[0][1] - zahyo[1][1]))
            
            


