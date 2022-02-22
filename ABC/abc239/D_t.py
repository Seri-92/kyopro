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

prime_set = set(range(2, 201))
set_ = set()

for i in range(2, 201):
    for j in range(2, 16):
        if i * j <= 200:
            set_.add(i * j)

prime_set = prime_set - set_

for i in range(a, b+1):
    flag = 1
    for j in range(c, d+1):
        if i + j in prime_set:
            flag = 0
            break

    if flag:
        print('Takahashi')
        exit()

print('Aoki')


