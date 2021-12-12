x, y = map(int, input().split())
cnt = 0

while True:
    if 2 ** cnt > y / x:
        break
    cnt += 1`

print(cnt)