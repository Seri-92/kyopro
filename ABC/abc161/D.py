k = int(input())
n = 0
cnt = 0
while True:
    n += 1
    lst = list(str(n))
    for i in range(len(str(n))-1):
        bif abs(int(lst[i+1]) - int(lst[i])) >= 2:
            cnt -= 1
            break
    cnt += 1
    if cnt >= k:
        print(n)
        exit() 
 
