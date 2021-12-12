n, W = map(int, input().split())
list_ = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 110000 for _ in range(110)]
dp[0]

for i in range(1, n+1):
    for j in range(W+1):
        w, v = list_[i]
        dp[i][j] = dp[i-1][j]
        if j >= w:
            dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v) 
print(dp[n][W])
