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

flag = True
S = [input() for _ in range(10)]
b = 9
for i in range(10):
    s = S[i]
    if flag:
        for j in range(10):
            if s[j] == '#':
                a = i
                c = j
                k = j
                while s[k] == '#':
                    k += 1
                    if k > 9:
                        break
                d = k - 1
                flag = False
                break
    if not flag:
        if s[c] != '#':
            b = i - 1
            break

a += 1
b += 1
c += 1
d += 1

print(a, b)
print(c, d)
            


