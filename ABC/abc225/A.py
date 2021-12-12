s = list(input())
s = set(s)
l = len(s)
if l == 1:
    ans = 1
elif l == 2:
    ans = 3
else:
    ans = 6
print(ans)