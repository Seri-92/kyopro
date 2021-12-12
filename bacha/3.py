n = int(input())
A = list(map(int, input().split()))
cnt = 0

while True:
    flag = 0
    for i in range(n):
        if A[i] %2 != 0:
            flag = 1
        else:
            A[i] = A[i] // 2
    if flag:
        print(cnt)
        exit()
    cnt += 1