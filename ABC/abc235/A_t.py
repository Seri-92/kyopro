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

x = ii()
c = x % 10
x //= 10
b = x % 10
x //= 10
a = x % 10

ans = (a + b + c) * 111
print(ans)
