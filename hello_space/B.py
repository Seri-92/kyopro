n, D, H = map(int, input().split())
syahei = [list(map(int, input().split())) for _ in range(n)]
lst = []
for i in range(n):
    d, h = syahei[i]
    lst.append(h - d * (H - h)/(D - d))
ans = max(0, max(lst))
print(ans)