a, b, c = map(int, input().split())
if 4 * a * b < (a + b -c) ** 2 and a + b - c < 0:
    print("Yes")
else:
    print("No")


