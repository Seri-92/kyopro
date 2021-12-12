s = list(input())
for i in range(4):
    s[i] = int(s[i])
ans = 'Strong'
if len(set(s)) == 1:
    ans = 'Weak'
if all([s[i+1] == (s[i] + 1) % 10 for i in range(3)]):
    ans = 'Weak'
print(ans)