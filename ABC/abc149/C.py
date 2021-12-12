import math
x = int(input())
while True:
    ok = True
    for j in range(2, int(math.sqrt(x))+1):
        if x % j == 0:
            ok = False
    if ok:
        print(x)
        exit() 
    x += 1

            
        
            