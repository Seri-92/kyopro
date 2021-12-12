n, m = map(int, input().split())
lst = [list(input().split()) for _ in range(m)]

ans = [''] * 3
for [s, c] in lst:
    s = int(s) - 1
    if ans[s] in ['', c]:
        ans[s] = c 
    else:
        print(-1)
        exit()


if n == 1:
    if m == 0:
        print(0)
        exit()
    else:
        ans = ans[0]
        print(ans)
        exit()

if n == 2 and m == 0:
    print(10)
    exit()

if n == 3 and m == 0:
    print(100)
    exit()

if ans[0] == '0':
    print(-1)
    exit()

if ans[0] == '':
    ans[0] = '1'

if ans[1] == '':
    ans[1] = '0'

if ans[2] == '':
    ans[2] = '0'

if n == 2:
    ans.pop()
ans = ''.join(ans)
print(ans)