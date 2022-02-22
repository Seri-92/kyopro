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
s = li() 

r = []
l = []

for i in range(n):
    x = s[i]
    if x == 'L':
        r.append(i)
    else:
        l.append(i)

ans = l + [n] + r[::-1]
print(*ans)
