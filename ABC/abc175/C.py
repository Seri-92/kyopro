x, k , d = map(int, input().split())
if abs(x) > k * d:
    print(abs(abs(x) - k * d))
    exit()

else:
    x = abs(x)
    q = x // d
    r = x % d
    if (q - k) % 2 == 0:
        print(r)
    else:
        print(abs(r-d))
    