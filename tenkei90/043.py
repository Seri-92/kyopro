from collections import deque
h, w = map(int, input().split())
rs, cs = map(int, input().split())
rs -= 1
cs -= 1

rt, ct = map(int, input().split())
rt -= 1
ct -= 1
board = [list(input()) for _ in range(h)]
dp = [[[-1] * 4 for _ in range(w)] for _ in range(h)]
todo = deque([[rs, cs, 0], [rs, cs, 1], [rs, cs, 2], [rs, cs, 3]])
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dp[rs][cs] = [0, 0, 0, 0]
while todo:
    crr = todo.popleft()
    r, c = crr[:2]
    direction = crr[2]
    nxt = crr
    for i in range(4):
        mr, mc = move[i]
        nxt[0] += mr
        nxt[1] += mc
        nxt[2] = i
        nr, nc = nxt[:2]
        if nr >= h or nr < 0 or nc >= w or nc < 0:
            continue
        if board[nr][nc] == '#':
            continue
        if dp[nr][nc][i] < 0:
            if i == direction:
                dp[nr][nc][i] = dp[r][c][direction]
            else:
                dp[nr][nc][i] = dp[r][c][direction]+1
            todo.append(nxt)

print(dp)

