import math

def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

n = int(input())

mod = 1000000007

fac_list = [1]
finv_list = [1]
inv_list = [modinv(i, mod) for i in range(n+1)]

for i in range(1, n+1):
    fac_list.append(fac_list[-1] * i % mod)
    finv_list.append(finv_list[-1] * inv_list[i] % mod)

for k in range(1, n+1):
    ans = 0
    a = 1
    while n - (k-1) * (a-1) >= a:
        m = n - (k-1) * (a-1)
        ans += fac_list[m] * finv_list[a] * finv_list[m-a] % mod
        ans %= mod
        a += 1
    print(ans)
    

