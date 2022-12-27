from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

s = li()

column = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]


all_0 = [1, 1, 2, 2, 2, 1, 1]

if s[0]:
    print('No')
    exit()



for i in range(10):
    if not s[i]:
        all_0[column[i]] -= 1

for i in range(7):
    for j in range(i+1, 7):
        for k in range(j+1, 7):
            if all_0[i] == 1 and all_0[j] == 0 and all_0[k] == 1:
                print('Yes')
                exit()

print('No')




