from collections import defaultdict
n = int(input())
N = 1001
board = [[0] * N for _ in range(N)]
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())

    # マス目に直す
    rx -= 1
    ry -= 1

    board[lx][ly] += 1
    board[lx][ry+1] += -1
    board[rx+1][ly] += -1
    board[rx+1][ry+1] += 1

for i in range(N):
    for j in range(N-1):
        board[i][j+1] += board[i][j]

for i in range(N-1):
    for j in range(N):
        board[i+1][j] += board[i][j]


d = defaultdict(int)
for i in range(N):
    for j in range(N):
        d[board[i][j]] += 1

for i in range(1, n+1):
    print(d[i])
