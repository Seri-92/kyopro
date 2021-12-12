K, S = map(int, input().split())
ans = 0
for X in range(min(K, S)+1):
    for Y in range(min(K, S-X)+1):
        if 0 <= S-X-Y <= K:
            ans += 1 
print(ans) 