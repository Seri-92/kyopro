n = int(input())
P = list(map(int, input().split()))
cnt = 0
for i in range(n-2):
    l = P[i:i+3]
    if l[1] == sorted(l)[1]:
        cnt += 1
    
print(cnt)
