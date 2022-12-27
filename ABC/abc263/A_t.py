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

l = lmi()
l.sort()

def judge_full_house(l):
    a, b, c, d, e = l

    if a == b and b == c:
        if d == e and c != d:
            return True
    if a == b:
        if b != c and c == d and d == e:
            return True
    return False

print('Yes' if judge_full_house(l) else 'No')
