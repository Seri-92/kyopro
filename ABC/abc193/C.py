n = int(input())
out = set()
a = 2
while a ** 2 <= n:
    b = 2
    while a ** b <= n:
        out.add(a**b)
        b += 1
    a += 1

print(n - len(out))
