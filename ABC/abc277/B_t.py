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

def judge(s_list):
    s_set = set(s_list)
    if len(s_set) != len(s_list):
        return False

    for s in s_list:
        if s[0] not in {'H', 'D', 'C', 'S'}:
            return False
        if s[1] not in set(list('A23456789TJQK')):
            return False

    return True

n = ii()
s_list = [input() for _ in range(n)]
print('Yes' if judge(s_list) else 'No')
