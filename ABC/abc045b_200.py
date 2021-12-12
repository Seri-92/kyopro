S = [input() for _ in range(3)]
t = 0
i = [0, 0, 0]
while len(S[t]) > i[t]: 
    tmp = t
    if S[t][i[t]] == "a":
        t = 0
    elif S[t][i[t]] == "b":
        t = 1
    else:
        t = 2
    i[tmp] += 1
if t == 0:
    ans = "A"
elif t == 1:
    ans = "B"
else:
    ans = "C"
print(ans)
