s = input()
ans = ''
for c in s:
    if c == '0' or c == '1':
        ans += c
    else:
        if c:
            ans = ans[:-1]
print(ans)