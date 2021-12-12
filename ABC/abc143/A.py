a, b = map(int, input().split())
rest = a - b * 2
if rest < 0:
    rest = 0
print(rest)