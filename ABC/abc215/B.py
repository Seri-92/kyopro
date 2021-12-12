n = int(input())
for i in range(100000):
    if 2 ** i > n:
        print(i-1)
        exit()