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

n, q = mi()
value_list = list(range(n + 1))
position_list = list(range(n + 1))

for _ in range(q):
    x = ii()
    x_pos = position_list[x]
    if x_pos < n:
        position_list[x] += 1
        position_list[value_list[x_pos+1]] -= 1
        value_list[x_pos], value_list[x_pos+1] = value_list[x_pos+1], value_list[x_pos]
    else:
        position_list[x] -= 1
        position_list[value_list[x_pos-1]] += 1
        value_list[x_pos], value_list[x_pos-1] = value_list[x_pos-1], value_list[x_pos]

print(*value_list[1:])
