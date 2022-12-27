from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# sys.setrecursionlimit(10**7)
# mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n = ii()
s = ls()
ans = ''
ab_num_tmp = {'A': 0, 'B': 0}
for i in range(n):
    if s[i] == 'C':
        ans += 'A' * (ab_num_tmp['A'] + (ab_num_tmp['B']//2)) + 'B' * (ab_num_tmp['B']%2)
        ans += 'C'
        ab_num_tmp = {'A': 0, 'B': 0}
        
    else:
        ab_num_tmp[s[i]] += 1

ans += 'A' * (ab_num_tmp['A'] + (ab_num_tmp['B']//2)) + 'B' * (ab_num_tmp['B']%2)
print(ans)
