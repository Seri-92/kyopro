n = int(input())
ans = 0
for a in range(1, int(10**(11/3))+1):
    for b in range(a, int((0--n//a) ** (1/2))+1):
        ans += max(n // (a * b) - b + 1, 0)
print(ans)