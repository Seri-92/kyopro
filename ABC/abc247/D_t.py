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

cylinder = deque()
q = ii()
for i in range(q):
    query = lmi()
    if query[0] == 1:
        cylinder.append(query[1:])
    else:
        c = query[1]
        ans = 0
        while c:
            x, num = cylinder.popleft()
            t = min(c, num)
            ans += t * x
            c -= t
            num -= t
            if num:
                cylinder.appendleft([x, num])
        print(ans)

