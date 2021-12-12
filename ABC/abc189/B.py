n, x = map(int, input().split())
x *= 100
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    v, p = lst[i]
    x -= v * p
    if x < 0:
        print(i+1)
        exit()
print(-1)  
