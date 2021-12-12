k, x = map(int, input().split())
bottom = x - k + 1
top = x + k - 1
ans = []

for i in range(bottom, top + 1):
    ans.append(i)

print(*ans)