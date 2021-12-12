n = int(input())
A = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(n)]
for j in range(10):
    if A[0] == j:
        dp[0][j] = 1
    else:
        dp[0][j] = 0
 
for i in range(1, n):
    for j in range(10):
        dp[i][(j*A[i])%10] += dp[i-1][j] 
        dp[i][(j*A[i])%10] %= 998244353 
        dp[i][(j+A[i])%10] += dp[i-1][j] 
        dp[i][(j+A[i])%10] %= 998244353 

for j in range(10):
    print(dp[-1][j])
