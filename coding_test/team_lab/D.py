ans = 0
l = []
for i in range(1, 20001):
    flag = False
    if i % 3 == 0:
        flag = True
    elif '3' in str(i):
        flag = True
    if flag:
        ans += i
        l.append(i)

print(f'{ans}')
print(l[:10])
