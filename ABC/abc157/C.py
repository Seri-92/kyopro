N, M = map(int, input().split()) 
ans = ['', '', '']

lst = [list(input().split()) for _ in range(M)]
for [s, c] in lst:
    s = int(s)-1
    if ans[s] in ['', c]:
        ans[s] = c
    else:
        print(-1)
        exit()

if ans[0] == '0' and N >1:
    print(-1)
    exit()

if N == 3: 
    if M == 0:
        print(100)
        exit()    
    if ans[0] == '':
        ans[0] = '1'
    if ans[1] == '':
        ans[1] = '0'
    if ans[2] == '':
        ans[2] = '0'

if N == 2:
    
    if M == 0:
        print(10)
        exit()
    ans.pop()
    if ans[0] == '':
        ans[0] = '1'
    if ans[1] == '':
        ans[0] = '0'
    
if N == 1:
    if M == 0:
        print(0)
        exit()
    ans = ans[0]

print(''.join(ans))