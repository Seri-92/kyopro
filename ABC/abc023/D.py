n = int(input())
H = []
S = []
for i in range(n):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)
top = 10**18
bottom = 1
while top - bottom > 1:
    mid = (top + bottom) // 2
    T = []
    for i in range(n):
        T.append((mid - H[i]) // S[i])
    T.sort()
    flag = True
    for i in range(n):
        if T[i] < i:
            flag = False
            
    if flag:
        top = mid
    else:
        bottom = mid
print(top)
