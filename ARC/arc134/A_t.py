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

n, l, w = mi()
A =lmi()

x, y = 0, A[0]
ans = 0--(y-x)//w
for i in range(n-1):
    x, y = A[i], A[i+1]
    x += w
    ans += max(0--(y-x) // w, 0)
ans += max(0, 0--(l-A[-1]-w)//w)


print(ans)
