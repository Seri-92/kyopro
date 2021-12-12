N, K = map(int, input().split())
D = set(input())
while True:
    if D & set(str(N)):
         N += 1
         continue
    else:
        print(N)
        break
