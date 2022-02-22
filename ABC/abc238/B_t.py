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

A_sum = [0]
for i in range(n):
    A_sum.append((A_sum[-1] + A[i]) % 360)

A_sum.append(360)
A_sum.sort()
ans = 0
for i in range(len(A_sum)-1):
    ans = max(ans, A_sum[i+1] - A_sum[i])

print(ans)
