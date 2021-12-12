mod = 10 ** 9 + 7
n = int(input())
ans = pow(10, n, mod) - pow(9, n, mod ) * 2\
     + pow(8, n, mod)
ans %= mod
print(ans)