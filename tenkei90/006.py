n, k = map(int, input().split())
s = list(input())

l_idx = [[n+10] * (n+1) for _ in range(26)]
for i in range(26):
    for j in range(n-1, -1, -1):
        if s[j] == chr(ord('a') + i):
            l_idx[i][j] = j
        else:
            l_idx[i][j] = l_idx[i][j+1]

# print(l_idx)
ans = ''

idx_tmp = -1
while len(ans) < k:
    for i in range(26):
        if l_idx[i][idx_tmp+1] < n - k + 1 + len(ans):
            ans += chr(ord('a') + i)
            idx_tmp = l_idx[i][idx_tmp+1]
            break

print(ans)


    




