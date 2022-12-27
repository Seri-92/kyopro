s = input()
t = input()
l_s = len(s)
l_t = len(t)

dp = [[0] * (l_t+1) for _ in range(l_s+1)]

for i in range(1, l_s+1):
    for j in range(1, l_t+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

i = l_s
j = l_t
sna = ''
while True:
    if i <= 0 or j <= 0:
        break
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        sna += s[i-1]
        i -= 1
        j -= 1


ans = sna[::-1]


print(ans)

# print(dp[l_s][l_t])
