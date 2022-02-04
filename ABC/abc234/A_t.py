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

t = ii()

def f(x):
    return x ** 2 + 2 * x + 3

ans = f(f(f(t) + t) + f(f(t)))

print(ans)
