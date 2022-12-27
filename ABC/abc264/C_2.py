from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
import numpy as np

# sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

h_1, w_1 = mi()
A = [lmi() for _ in range(h_1)]
A = np.array(A)

h_2, w_2 = mi()
B = [lmi() for _ in range(h_2)]
B = np.array(B)


h_del_num = h_1 - h_2
w_del_num = w_1 - w_2

for x in combinations(list(range(w_1)), w_del_num):
    x = set(x)
    r_1, r_2 = 0, 0
    while True:
        flag = False
        A_tmp = []
        for i in range(w_1):
            if i not in x:
                A_tmp.append(A[r_1][i])
        for i in range(r_1, h_1):
            if A_tmp == B[i]:
                flag = True
                r_1 = i
                r_2 += 1
                break
        if not flag:
            break
    if r_2 == h_2:
        print('Yes')
        exit()

print('No')


