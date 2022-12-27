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

s1 = set()
for i in range(n):
    if A[i] == i+1:
        s1.add(i)
ans = len(s1) * (len(s1) - 1) // 2

for i in range(n):
    if A[i] == i+1:
        continue
    if A[A[i]-1] == i+1:
        if A[i] < i+1:
            ans += 1

print(ans)
        
        

