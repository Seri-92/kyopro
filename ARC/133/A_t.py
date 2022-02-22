from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n = ii()
A = lmi()
flag = 1
for i in range(n-1):
    x, y = A[i], A[i+1]
    if x > y:
        A_remove = x
        flag = 0
        break

if flag: A_remove = A[-1]

ans = []
for i in range(n):
    if A[i] != A_remove:
        ans.append(A[i])

print(*ans)
