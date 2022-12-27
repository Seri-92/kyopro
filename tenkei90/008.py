n = int(input())
s = '0' + input()
mod = 1000000007

dp = [[0] * 8 for _ in range(n+1)]
dp[0][0] = 1

ac = '0atcoder'

for i in range(1, n+1):
    for j in range(8):
        if j == 0:
            dp[i][j] = 1
            continue
        if s[i] == ac[j]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod

print(dp[n][7])
