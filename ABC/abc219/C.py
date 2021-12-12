x = list(input())
n = int(input())
S = [input() for _ in range(n)]
dict_ = dict()
for i in range(26):
    dict_[x[i]] = i
S_2 = []
for j in range(n):
    s = S[j]
    s_2 = ''
    for i in range(len(s)):
        s_2 += chr(dict_[s[i]] + ord('a'))
    S_2.append((s_2, j))
S_2.sort()
for i in range(n):
    print(S[S_2[i][1]])