W, a, b = map(int, input().split())
if abs(b-a) > W:
    print(abs(b-a)-W)
else:
    print(0)