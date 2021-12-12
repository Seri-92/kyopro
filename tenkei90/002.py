n = int(input())
for i in range(1 << n):
    s = [0] * n
    hiraku = 0
    flag = 0
    for j in range(n):
        if i & (1 << (n-j-1)):
            s[j] = ')'
            hiraku -= 1
        else:
            s[j] = '('
            hiraku += 1
        if hiraku < 0:
            flag = 1
    if flag:
        continue
    if hiraku > 0:
        continue
    print(''.join(s))
