n = int(input())
X, Y = map(int, input().split())
bento = [list(map(int, input().split())) for _ in range(n)]
print(bento)
inf = 500
dp = [[[inf for _ in range(Y+1)] for _ in range(X+1)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(1, n+1):
    for x in range(X+1):
        for y in range(Y+1):
            bento_x = bento[i-1][0]
            bento_y = bento[i-1][1]

            if x - bento_x >= 0 and y - bento_y >= 0:
                dp[i][x][y] = min(dp[i][x][y], dp[i-1][x - bento_x][y - bento_y]+1)
            dp[i][x][y] = min(dp[i-1][x][y], dp[i][x][y])
print(dp)
if dp[n][X][Y] == inf:
    print(-1)
else:
    print(dp[n][X][Y])