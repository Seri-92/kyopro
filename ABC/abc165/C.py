from itertools import combinations_with_replacement as cbw

n, m, q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(q)]
ans = []
for seq in cbw(range(1,m+1), n):
    d_sum = 0
    for i in range(q):
        a, b, c, d = lst[i]
        a -= 1
        b -= 1
        if seq[b]-seq[a] == c:
            d_sum += d
    ans.append(d_sum)
ans = max(ans)
print(ans)