import math

x, y, a, b = map(int, input().split())

boundary = b / (a-1)
cnt = 0

if x < boundary:
    num = math.ceil(math.log(boundary / x, a))
    x *= num * a
    cnt += num

cnt += (y-x-1) // b

print(cnt)