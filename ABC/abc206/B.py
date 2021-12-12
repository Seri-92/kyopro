n = int(input())
ans = 0
for i in range(1, 10**6):
    ans += i
    if ans > n:
        print(i)
        exit()
