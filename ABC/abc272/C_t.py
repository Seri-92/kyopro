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
A = lmi()
even_list = []
odd_list = []

for a in A:
    if a % 2 == 0:
        even_list.append(a)
    else:
        odd_list.append(a)

even_list.sort()
odd_list.sort()

if len(even_list) < 2 and len(odd_list) < 2:
    print(-1)
    exit()

ans = max(sum(even_list[-2:]), sum(odd_list[-2:]))
ans = 0
if len(even_list) >= 2:
    ans = max(ans, sum(even_list[-2:]))
if len(odd_list) >= 2:
    ans = max(ans, sum(odd_list[-2:]))
print(ans)
