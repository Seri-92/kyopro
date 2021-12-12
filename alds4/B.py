n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

ans = 0
for ti in t:
    top = len(s)-1
    bottom = 0
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if ti <= s[mid]:
            top = mid
        else:
            bottom = mid
    if ti == s[bottom] or ti == s[top]:
        ans += 1

print(ans)
