s = input()
d = dict()
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
for v in d.values():
    if v % 2 !=0:
        print("No")
        exit(0)
print("Yes")