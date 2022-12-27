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


def s_to_i(s):
    ret = []
    for i in range(len(s)):
        if s[i] == 'a':
            ret.append(0)
        elif s[i] == 't':
            ret.append(1)
        elif s[i] == 'c':
            ret.append(2)
        elif s[i] == 'o':
            ret.append(3)
        elif s[i] == 'd':
            ret.append(4)
        elif s[i] == 'e':
            ret.append(5)
        else:
            ret.append(6)
    return ret

s = list(input())

l = s_to_i(s)
ans = 0
for i in range(7):
    for j in range(i, 7):
        if l[i] > l[j]:
            ans += 1

print(ans)
