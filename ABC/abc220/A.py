a, b, c = map(int, input().split())
while True:
    if a > b:
        print(-1)
        exit()
    if a % c == 0:
        print(a)
        exit()
    a += 1 