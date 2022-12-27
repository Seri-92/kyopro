n, k = map(int, input().split())

cnt_list = [0] * (n+1)

for i in range(2, n+1):
    if cnt_list[i] != 0: continue
    for j in range(i, n+1, i):
        cnt_list[j] += 1


ans = 0
for i in range(n+1):
    if cnt_list[i] >= k:
        ans += 1

print(ans)
