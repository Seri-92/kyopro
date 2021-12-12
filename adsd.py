n, k = map(int, input().split())
l = list(input().split())

ans = n
while 1:
    for i in str(ans):
        if i in l:
            break
    else:
        break
    ans += 1

print(ans)