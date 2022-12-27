h, w = map(int, input().split())

board = [list(input()) for _ in range(h)]

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

mod = 10**9 + 7

if board[0][0] == '#':
    print(0)
    exit()



for i in range(h):
    for j in range(w):
        if board[i][j] == '#':
            continue
        if i == 0 and j == 0:
            continue
        elif j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] += dp[i][j-1]
            if i > 0:
                dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod

print(dp[-1][-1])
