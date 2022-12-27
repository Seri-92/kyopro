n = int(input())
A = list(map(int, input().split()))

inf = 10**10
dp = [[inf] * (2*n+1) for _ in range(2*n+1)]
for i in range(2*n-1):
    dp[i][i+2] = abs(A[i] - A[i+1])
for i in range(2, n+1):
    length = i * 2
    for l in range(2*n-1):

        r = l + length
        if r > 2 * n:
            break
        dp[l][r] = min(dp[l][r], dp[l+1][r-1] + abs(A[l] - A[r-1]))
        for k in range(2, length, 2):
            dp[l][r] = min(dp[l][r], dp[l][l+k] + dp[l+k][r])

print(dp[0][2*n])
