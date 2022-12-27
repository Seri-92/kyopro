def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b, c = map(int, input().split())
g = gcd(a, gcd(b, c))

ans = (a + b + c) // g - 3
print(ans)
