x, y = map(int, input().split())
if x == y:
    print(x)
    exit()
for i in range(3):
    if x == i:
        continue
    elif y == i:
        continue
    print(i)
    exit()
    