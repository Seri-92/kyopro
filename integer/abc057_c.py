n = int(input())
a = 1
ans = 100000000000
while a ** 2 <= n:
    if n % a == 0:
        b = n // a
        ans = min(ans, max(len(str(a)), len(str(b))))
    a += 1

print(ans)


