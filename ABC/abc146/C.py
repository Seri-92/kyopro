A, B, X = map(int, input().split())

def cost(n):
    return A * n + B * len(str(n))

if cost(1) > X:
    print(0)
    exit()

if cost(10**9) < X:
    print(10**9)
    exit()

bottom = 1
top = 10**9

while top - bottom > 1:
    mid = (top + bottom) // 2
    if cost(mid) <= X:
        bottom = mid
    else:
        top = mid

print(bottom)