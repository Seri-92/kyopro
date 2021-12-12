a, b = map(int, input().split())
if b == 1:
    print(0)
    exit()

x = 1
i = 0
while x < b:
    x += (a - 1)
    i += 1

print(i)