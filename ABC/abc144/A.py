a, b = input().split()

if len(a) == 1 and len(b) == 1:
    a = int(a)
    b = int(b)
    print(a * b) 
else:
    print(-1)