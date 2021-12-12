s = input()
t = input()
ans = 0
A = []
for i in range(len(s)-len(t)+1):
    s_i = s[i:i+len(t)+1]
    count = 0
    for j in range(len(t)):
        if s_i[j] == t[j]:
            count += 1
    A.append(count)

ans = len(t) - max(A)
print(ans)