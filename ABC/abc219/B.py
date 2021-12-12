S = []
for i in range(3):
    S.append(input())
t = list(input())
ans = []
for x in t:
    x = int(x) - 1
    ans.append(S[x])
print(''.join(ans))
