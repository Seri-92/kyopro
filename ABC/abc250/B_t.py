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

n, a, b = mi()

for k in range(n):
    if k % 2 == 0:
        for i in range(a):
            s = ''
            for j in range(n):
                if j % 2 == 0:
                    s += '.' * b
                else:
                    s += '#' * b
            print(s)
    else:
        for i in range(a):
            s = ''
            for j in range(n):
                if j % 2 == 0:
                    s += '#' * b
                else:
                    s += '.' * b
            print(s)



