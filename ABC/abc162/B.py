n = int(input())
ans = []
for i in range(1, n+1):
    if i % 3 != 0 and i % 5 != 0:
        ans.append(i)
ans = sum(ans)
print(ans)