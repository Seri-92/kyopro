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

n = ii()
submission_list = []

for _ in range(n):
    s, t = input().split()
    t = int(t)
    submission_list.append([s, t])

string_set = set()
original_list = []
for i in range(n):
    s_tmp = submission_list[i][0]
    if s_tmp not in string_set:
        original_list.append((-submission_list[i][1], i))
        string_set.add(s_tmp)

original_list.sort()
print(original_list[0][1] + 1) 
