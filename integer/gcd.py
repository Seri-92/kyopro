def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        print(x, y)
    return x

print(gcd(119, 32))

