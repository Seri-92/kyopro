
def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(mi())
def li(): return list(input())

s = input()
t = input()

l = len(s)

k = (ord(s[0]) - ord(t[0])) % 26

for i in range(l):
    x, y = s[i], t[i]
    if (ord(s[i]) - ord(t[i])) % 26 != k:
        print('No')
        exit()

print('Yes')


