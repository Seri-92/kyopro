n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
for i in range(1000):
    i = str(i)
    if len(i) != n:
        continue
    for [x, y] in lst:
        if i[x-1] != str(y):
            break
    else: 
        print(i)
        exit()

print(-1)
    
