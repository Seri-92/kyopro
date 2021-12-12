n = int(input())

d = 0
ans = n
while True:
    d += 1
    if n < 2**d:
        break
    q = n // (2**d)
    r = n % (2**d)
    b = d
    ans = min(ans, r+q+b)
    
print(ans)