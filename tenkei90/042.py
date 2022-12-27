import math
k = int(input())
mod = 1000000007



def solve(k):
    if k % 9 != 0:
        return 0
    
    dp = [0] * (k+1)
    for i in range(1, 10):
        dp[i] += 1
    for i in range(k+1):
        for j in range(1, 10):
            if i - j > 0:
                dp[i] += dp[i-j]
                dp[i] %= mod

    return dp[k]
        

print(solve(k))
