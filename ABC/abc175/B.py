n = int(input())
l = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a = l[i]
            b = l[j]
            c = l[k]
            if not len(set([a, b, c])) == 3:
                continue
            if abs(a-b) < c < a + b:
                cnt += 1
                
print(cnt)