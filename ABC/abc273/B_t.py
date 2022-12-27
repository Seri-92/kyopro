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

x, k = mi()
x = list(map(int, str(x)))
x = x[::-1]
l = len(x)

if l < k:
    print(0)
    exit()

def round_off(x, i):
    if x[i] < 5:
        x[i] = 0
    else:
        x[i] = 0
        while i <= l-1:
            if i == l-1:
                x.append(1)
                return
            if x[i+1] < 9:
                x[i+1] += 1
                return
            else:
                x[i+1] = 0
                i += 1

for i in range(k):
    round_off(x, i)

ans = ''
x = x[::-1]
for i in range(len(x)):
    ans += str(x[i])
    
print(int(ans))
