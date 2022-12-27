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

t = ii()

def max_periodic(n):
    l = len(str(n))
    periodic_list = []
    periodic_list.append(int('9' * (l - 1)))
    for i in range(1, l//2+1):
        if l % i != 0:
            continue
        # if str(n)[0] != '1':
        #     y = str((int(str(n)[0]) - 1)) + ('9' * (l // i - 1))
        #     y = int(y)
        #     periodic_list.append(y)
        x = int(str(n)[:i] * (l // i))
        if x <= n:
            periodic_list.append(x)
        z = int(str(int(str(n)[:i]) - 1) * (l // i))
        periodic_list.append(z)
    return max(periodic_list)

for _ in range(t):
    n = ii()
    print(max_periodic(n))
