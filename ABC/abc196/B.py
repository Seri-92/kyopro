x = input()
ans = ''
if not '.' in x:
    print(x)
    exit()

for i in range(len(x)):
    if x[i] == '.':
        break
    ans += x[i]
print(ans)