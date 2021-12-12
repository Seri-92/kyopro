n, m = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
koho = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for i in range(1<<k):
    switches = [0] * k
    for j in range(k):
        switches[j] = i >> j & 1
    sara_set = set()
    for j in range(k):
        sara_set.add(koho[j][switches[j]])
    cnt = 0
    for j in range(m):
        if conditions[j][0] in sara_set and conditions[j][1] in sara_set:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
