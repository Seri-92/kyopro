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

a, b, c, d, e, f, x = mi()

l_takahashi = x // (a + c) * a * b + min(x % (a + c) * b, a * b)
l_aoki = x // (d + f) * d * e + min(x % (d + f) * e, d * e)

# print(l_takahashi)
# print(l_aoki)
if l_takahashi > l_aoki:
    ans = 'Takahashi'
elif l_takahashi == l_aoki:
    ans = 'Draw'
else:
    ans = 'Aoki'

print(ans)
