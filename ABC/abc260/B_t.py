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

n, x, y, z = mi()
A = lmi()
B = lmi()
ans = []
l_1 = [[A[i], -i, B[i]] for i in range(n)]
l_1.sort()
for i in range(x):
    ans.append(l_1[n-1-i][1])
l_tmp = l_1[:n-x]
l_2 = []
for i in range(n-x):
    a, idx, b = l_tmp[i]
    l_2.append([b, idx, a])

l_2.sort()
for i in range(y):
    ans.append(l_2[len(l_2)-1-i][1])
l_tmp = l_2[:n-x-y]
l_3 = []
for i in range(n-x-y):
    b, idx, a = l_tmp[i]
    l_3.append([a+b, idx])
l_3.sort()

for i in range(z):
    ans.append(l_3[len(l_3)-1-i][1])

ans.sort(reverse=True)

for a in ans:
    print(-a+1)
