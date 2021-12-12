x = int(input())

while True:
    ok = True
    i = 2
    while i ** 2 < x+1:
        if x % i == 0:
            ok = False
        i += 1
    if ok:
        print(x)
        exit()
    x += 1
    
