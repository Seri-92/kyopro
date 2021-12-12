s = input()
max = s
min = s
l = len(s)
for i in range(l):
    s = s[1:] + s[0]
    if s > max:
        max = s
    if s < min:
        min = s
print(min)
print(max)
