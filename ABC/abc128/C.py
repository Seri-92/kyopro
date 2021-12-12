n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))

P = list(map(int, input().split()))
ans = 0

for i in range(2**n):
    switchs = [0] * (n+1)
    for j in range(1, n+1):
        switchs[j] = i >> (j-1) & 1
    flag = 1
    for k in range(m):
        if sum([switchs[lst[k][l]] for l in range(1, lst[k][0]+1)]) %2 != P[k]:
            flag = 0
    if flag:
        ans += 1

print(ans)