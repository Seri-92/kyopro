mod = 998244353
a, b, c = map(int, input().split())
ans = 1
ans *= a * (a+1) // 2
ans %= mod
ans *= b * (b+1) // 2
ans %= mod
ans *= c * (c+1) // 2
ans %= mod

print(ans)