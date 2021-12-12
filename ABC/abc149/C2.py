x = int(input())
while True:
    x += 1
    i = 2
    while i * i <= x:
        if x % i == 0:
            break
        i += 1
    else: 
        print(x)
        break


