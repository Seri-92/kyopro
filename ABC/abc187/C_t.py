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
exclamation_set = set()
non_exclamation_set = set()
for _ in range(n):
    s = input()
    if s[0] == '!':
        exclamation_set.add(s[1:])
    else:
        non_exclamation_set.add(s)

for s in exclamation_set:
    if s in non_exclamation_set:
        print(s)
        exit()

print('satisfiable')
