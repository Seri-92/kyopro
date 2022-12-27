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

a, b = mi()

def f(x):
    ret = []
    if x == 1:
        ret = [0]
    elif x == 2:
        ret = [1]
    elif x == 3:
        ret = [0, 1]
    elif x == 4:
        ret = [2]
    elif x == 5:
        ret = [0, 2]
    elif x == 6:
        ret = [1, 2]
    elif x == 7:
        ret = [0, 1, 2]
    return ret

l = [1, 2, 4]
ans = 0
for i in range(3):
    if i in f(a) or i in f(b):
        ans += l[i]

print(ans)
