n, k = map(int, input().split())
H = list(map(int, input().split()))
inf = 10 ** 18
dp = [inf] * n
dp[0] = 0

for i in range(1, n):
    for j in range(1, k+1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(H[i] - H[i-j]))
        
print(dp[-1])
