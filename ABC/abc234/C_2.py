k = int(input())
ans = list(bin(k))[2:]
for i in range(len(ans)):
    if ans[i] == '1':
        ans[i] = '2'
print(''.join(ans))
