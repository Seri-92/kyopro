s = input()
n = len(s)
flag = True
for i in range(n):
    if i % 2 == 0:
        if s[i].isupper():
            flag = False
    else:
        if s[i].islower():
            flag = False

if flag:
    print('Yes')
else:
    print('No')
