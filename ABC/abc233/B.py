from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

l, r = mi()
l -= 1
r -= 1
s = li()


ans =s[:l] + s[l:r+1][::-1] + s[r+1:]

print(''.join(ans))


