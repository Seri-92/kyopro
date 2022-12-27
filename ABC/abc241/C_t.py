from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, accumulate
import sys
import math
import bisect

# sys.setrecursionlimit(10**7)
# mod = 1000000007

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def ls(): return list(input())
def li(): return list(map(int, str(input())))

n = ii()
board = [ls() for _ in range(n)]

column_list = []

for i in range(n):
    column = []
    for j in range(n):
        column.append(board[j][i])
    column_list.append(column)

def hash_count(s):
    cnt = 0
    for x in s:
        if x == '#':
            cnt += 1
    return cnt
            

for i in range(n):
    row = board[i]
    for j in range(n-5):
        row_tmp = row[j:j+6]
        if hash_count(row_tmp) >= 4:
            print('Yes')
            exit()

for i in range(n):
    column = column_list[i]
    for j in range(n-5):
        column_tmp = column[j:j+6]
        if hash_count(column_tmp) >= 4:
            print('Yes')
            exit()

diagonal_list = []
for i in range(n):
    diagonal = []
    for j in range(n):
        if i + j >= n:
            break
        diagonal.append(board[0+j][i+j])
    diagonal_list.append(diagonal)
    
for i in range(n):
    diagonal = []
    for j in range(n):
        if i + j >= n:
            break
        diagonal.append(board[i+j][0+j])
    diagonal_list.append(diagonal)

for i in range(n):
    diagonal = []
    for j in range(n):
        if i - j < 0:
            break
        diagonal.append(board[0+j][i-j])
    diagonal_list.append(diagonal)

for i in range(n):
    diagonal = []
    for j in range(n):
        if i + j >= n:
            break
        diagonal.append(board[i+j][n-1-j])
    diagonal_list.append(diagonal)

for diagonal in diagonal_list:
    for j in range(n-5):
        diagonal_tmp = diagonal[j:min(j+6, len(diagonal))]
        if hash_count(diagonal_tmp) >= 4 and len(diagonal) >= 6:
            print('Yes')
            exit()

print('No')
