s = list(input())
t = list(input())

for i in range(len(s)):
    if s[i] != t[i]:
        print('No')
        exit()

print('Yes')    