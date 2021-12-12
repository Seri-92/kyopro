n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
while k >= 0:  
    if a == [] and b == []:
        break
    elif a == []:
        choice = b[0]
        b.pop(0)
        ans += 1
        continue
    elif b == []:
        choice = a[0]
        a.pop()
        ans += 1
        continue
    else:
        choice = min(a[0], b[0])
    if k >= choice:
        k -= choice
        ans += 1
        if choice == a[0]:
            a.pop(0)
        else:
            b.pop(0)
    else:
        break

print(ans)
