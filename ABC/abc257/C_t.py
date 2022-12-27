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

def cnt_correct(x):
    cnt = 0
    for i in range(n):
        w = W[i]
        if w >= x:
            if int(s[i]):
                cnt += 1
        else:
            if not int(s[i]):
                cnt += 1
    return cnt

n = ii()
s = input()
W = lmi()

adults = []
childs = []

for i in range(n):
    if int(s[i]):
        adults.append(W[i])
    else:
        childs.append(W[i])

adults.sort()
childs.sort()

ans = 0
l = len(adults)
ans = max(l, n-l)
for i, x in enumerate(adults):
    cnt = l - i + bisect_left(childs, x)
    ans = max(ans, cnt)

print(ans)
