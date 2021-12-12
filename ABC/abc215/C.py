from itertools import permutations
s, k = input().split()
k = int(k)
s = list(permutations(list(s)))
for i in range(len(s)):
    s[i] = ''.join(s[i])
s = list(set(s))
s.sort()
print(s[k-1])

