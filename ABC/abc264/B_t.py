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

r, c = mi()
r -= 1
c -= 1

board = [
        '#' * 15, '#' + '.'*13 + '#', '#.' + '#'* 11 + '.#',
        '#.#' + '.'*9 + '#.#', '#.#.' + '#'*7 + '.#.#',
        '#.#.#' + '.'*5 + '#.#.#', '#.#.#.###.#.#.#'
        ]
board = board + ['#.#.#.#.#.#.#.#'] + board[::-1]

print('black' if board[r][c] == '#' else 'white')
