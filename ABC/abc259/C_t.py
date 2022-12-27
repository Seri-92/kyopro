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

s = input()
t = input()

def rle(s):
    list_ = []
    x_tmp = s[0]
    num = 0
    for x in s:
        if x == x_tmp:
            num += 1
        else:
            list_.append([x_tmp, num])
            x_tmp = x
            num = 1
    list_.append([x_tmp, num])
    return list_

s_list = rle(s)
t_list = rle(t)

if len(s_list) != len(t_list):
    print('No')
    exit()

flag = True
for i in range(len(s_list)):
    if s_list[i][0] != t_list[i][0]:
        flag = False
        break
    if s_list[i][1] > t_list[i][1]:
        flag = False
        break
    if s_list[i][1] < t_list[i][1]:
        if s_list[i][1] == 1:
            flag = False
            break
    
print('Yes' if flag else 'No')
