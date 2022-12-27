n = int(input())
job_list = [list(map(int, input().split())) for _ in range(n)]
job_list.sort()

dp = [[0] * 5005 for _ in range(n+5)]

for i in range(1, n+1):
    d, c, s = job_list[i-1]
    for j in range(5005):
        dp[i][j] = dp[i-1][j]
        if c <= j <= d:
            dp[i][j] = max(dp[i-1][j-c] + s, dp[i][j])
print(max(dp[n]))
