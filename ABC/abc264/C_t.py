from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
import time
import numpy as np

# sys.setrecursionlimit(10**7)
# mod = 1000000007
# mod = 998244353

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

start_time = time.time()

h_1, w_1 = mi()
A = [lmi() for _ in range(h_1)]
A = np.array(A)

h_2, w_2 = mi()
B = [lmi() for _ in range(h_2)]
B = np.array(B)


h_del_num = h_1 - h_2
w_del_num = w_1 - w_2


h_del_idx = []
w_del_idx = []


for x in combinations(list(range(h_1)), h_del_num):
    h_del_idx = list(x)
    for x in combinations(list(range(w_1)), w_del_num):
        w_del_idx = list(x)
        A_2 = np.delete(A, h_del_idx, 0)
        A_2 = np.delete(A_2, w_del_idx, 1)

        # if np.allclose(A_2, B):
        #     print('Yes')
        #     exit()
        if np.all(A_2 == B):
            print('Yes')
            exit()
print('No')




