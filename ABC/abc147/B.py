s = input()
l = len(s) // 2

ans = 0
for i in range(l):
    if s[i] != s[-(i+1)]:
        ans += 1

print(ans)

