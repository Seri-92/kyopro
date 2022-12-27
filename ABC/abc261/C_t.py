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


s_dict = defaultdict(lambda:-1)

for i in range(n):
    s_tmp = input()
    s_dict[s_tmp] += 1
    if s_dict[s_tmp] > 0:
        print(s_tmp + f'({s_dict[s_tmp]})')
    else:
        print(s_tmp)
