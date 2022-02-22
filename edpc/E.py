n, w_max = map(int, input().split())
list_ = [0] + [list(map(int, input().split())) for _ in range(n)]

inf = 10**14

dp = [[inf] * 101000 for _ in range(n+1)]

dp[0][0] = 0

for i in range(1, n+1):
    for j in range(101000):
        w, v = list_[i]
        if j >= v:
            dp[i][j] = min(dp[i][j], dp[i-1][j-v] + w)
        dp[i][j] = min(dp[i][j], dp[i-1][j])


ans = 0
for i in range(101000):
    x = dp[-1][i]
    if x <= w_max:
        ans = max(ans, i)


print(ans)


