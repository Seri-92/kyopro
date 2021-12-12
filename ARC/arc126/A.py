t = int(input())
cases = []
for _ in range(t):
    cases.append(list(map(int, input().split())))

def main(a, b, c):
    ans = 0
    b //= 2
    if b > c:
        ans += c
        b -= c
        c = 0
    else:
        ans += b 
        c -= b
        b = 0
    if b > (a // 2):
        ans += a // 2   
        b -= a // 2
        a %= 2
    else:
        ans += b
        a -= b * 2
    if c > a * 2:
        ans += a
        a -= c//2
        c = 0
    else:
        ans += c//2 
        a -= c//2
        c %= 2
        ans += (2 * a + 4 * c) // 10

    return ans

for i in range(t):
    a, b, c = cases[i]
    print(main(a, b, c))