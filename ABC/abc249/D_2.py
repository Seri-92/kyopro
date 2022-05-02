from collections import defaultdict, deque, Counter
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
M = max(A)
ans = 0

c = Counter(A)

for x in c:
    a = 1
    while a ** 2 <= x:
        if x % a == 0:
            b = x // a
            ans += c[a] * c[b] * c[x] 
            if a != b:
                ans += c[a] * c[b] * c[x] 
        a += 1
print(ans)
