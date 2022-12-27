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
coord = [lmi() for _ in range(n)]
s = input()
dict_ = dict()

for i in range(n):
    x, y = coord[i]
    s_i = s[i]
    if y not in dict_:
        dict_[y] = [[x, s_i]]
    else:
        dict_[y].append([x, s_i])
    
for y in dict_:
    l = dict_[y]
    l.sort()
    hidari_r = -1
    for i in range(len(l)):
        if l[i][1] == 'R':
            hidari_r = i 
            break
    if hidari_r >= 0:
        for i in range(hidari_r + 1, len(l)):
            if l[i][1] == 'L':
                print('Yes')
                exit()
print('No')
