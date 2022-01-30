from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(10**7)
mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())


n = ii()
N = n
# N: 処理する区間の長さ
N0 = 2**(N-1).bit_length()
INF = 2**31-1
data = [INF]*(2*N0)
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = min(data[2*k+1], data[2*k+2])
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])

        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s


s = list(input())
for i in range(n):
    s[i] = ord(s[i])
for i in range(n):
    update(i, s[i])
j = n-1
for i in range(n):
    if i >= j:
        break
    r = s[i]
    x = query(i, j+1)
    if r == x:
        continue
    while True:
        l = s[j]
        if l == x:
            s[i], s[j] = s[j], s[i]
            j -= 1
            break
        if j == i:
            break
        j -= 1

for i in range(n):
    s[i] = chr(s[i])
print(''.join(s))
