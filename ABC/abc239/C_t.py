from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
# mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

a, b, c, d = mi()

def kouho_set(x, y):
    set_ = {(x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2),
            (x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1)}
    return set_

if kouho_set(a, b) & kouho_set(c, d):
    print('Yes')
else:
    print('No')
