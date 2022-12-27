a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b 
    return a

ans = a * b // gcd(a, b)
print(ans if ans <= 10**18 else 'Large')
