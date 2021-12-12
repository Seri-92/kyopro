n = int(input())
list_ = [list(map(int, input().split())) for _ in range(n)]
t = 0
for i in range(n):
    a, b = list_[i]
    t += a / b
    list_[i].append(a / b)
t /= 2
ans = 0
for i in range(n):
    x = list_[i][2]
    if t < x:
        ans += t * list_[i][1]
        break
    t -= x
    ans += list_[i][0]

print(ans)
