s = list(input())
ans = 0
for i in range(len(s)):
    ans += int(s[i])
ans *= 111
print(ans)
