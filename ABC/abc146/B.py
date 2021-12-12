n = int(input())
s = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
for i in s:
    ans += alphabet[(alphabet.index(i)+n)%26]
print(ans)
