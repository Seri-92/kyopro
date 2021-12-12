n = int(input())
S = list(map(int, input().split()))
ans = 0
for s in S:
    flag = True
    for a in range(1, 250):
        for b in range(1, 250):
            if 4 * a * b + 3 * (a + b) == s:
                flag = False
    
    if flag:
        ans += 1
print(ans)