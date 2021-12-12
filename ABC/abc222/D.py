n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 998244353
dp = [[0] * 3001 for _ in range(n)]
a = A[0]
b = B[0]

dp[0][