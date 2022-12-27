board = [[0] * 32 for _ in range(32)]

cnt = 0
c_tmp = 'A'
i = 0
j = 0
flag = 0
muki = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(32 * 32):
    board[i][j] = c_tmp
    if 0 > i + muki[flag][0] or i + muki[flag][0] > 31 or 0 > j + muki[flag][1] or j + muki[flag][1] > 31:
        flag += 1
        flag %= 4
    elif board[i+muki[flag][0]][j+muki[flag][1]] != 0:
        flag += 1
        flag %= 4
    i += muki[flag][0]
    j += muki[flag][1]
    if c_tmp == 'Z':
        cnt = 0
        c_tmp = 'A'
    else:
        cnt += 1
        c_tmp = chr(65 + cnt)

ans = ''
for i in range(32):
    ans += board[i][i]
print(ans)
print(board[0])
