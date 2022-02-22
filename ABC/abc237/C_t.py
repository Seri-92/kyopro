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

s = li()
n = len(s)

def is_kaibun(s):
    if s == s[::-1]:
        return True

if is_kaibun(s):
    print('Yes')
    exit()

forward = 0
back = 0
for i in range(n):
    if s[i] == 'a':
        forward += 1
    else:
        break
for i in range(n):
    if s[n-1-i] == 'a':
        back += 1
    else:
        break
s = ''.join(s)
if forward <= back:
    s = 'a' * (back - forward) + s
else:
    print('No')
    exit()
if is_kaibun(s):
    print('Yes')
else:
    print('No')
