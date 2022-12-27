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


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

n = ii()
s_x, s_y, t_x, t_y = mi()
circles = [lmi() for _ in range(n)]

for i in range(n):
    c_x, c_y, r = circles[i]
    if (s_x - c_x)**2 + (s_y - c_y)**2 == r**2:
        s_circle = i
    if (t_x - c_x)**2 + (t_y - c_y)**2 == r**2:
        t_circle = i

uf = UnionFind(n)

for i in range(n):
    c_1_x, c_1_y, r_1 = circles[i]
    for j in range(i+1, n):
        c_2_x, c_2_y, r_2 = circles[j]
        l = (c_1_x - c_2_x)**2 + (c_1_y - c_2_y)**2
        if l < max(r_1, r_2) - min(r_1, r_2):
            continue
        if l <= (r_1 + r_2)**2:
            uf.union(i, j)

if uf.same(s_circle, t_circle):
    print('Yes')
else:
    print('No')

