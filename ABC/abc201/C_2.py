s = input()
ans = 0
for i in range(10**4):
    num = f'{i:0=4}'
    flag = 1
    for j in range(10):
        if s[j] == 'x':
            if str(j) in num:
                flag = 0
        elif s[j] == 'o':
            if str(j) not in num:
                flag = 0
    if flag: ans += 1

print(ans)
