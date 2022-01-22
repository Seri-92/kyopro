from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right

# sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

n, k = mi()
A = lmi()
sum_A = [0] + list(accumulate(A))
for i in range(len(sum_A)):
    sum_A[i] = (sum_A[i], i)

sum_A.sort()

ans = 0
for i in range(len(sum_A)):
    x = sum_A[i]
    y_l = bisect_left(sum_A[]), x + k)
    y_r = bisect_right(sorted(sum_A[i:]), x + k)
    ans += max(0, y_r - y_l)
print(ans)
