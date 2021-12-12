x = int(input())
y = 100
ans = 0
while True:
    y = y * 101 // 100
    ans += 1
    if y >= x:
        print(ans)
        exit()