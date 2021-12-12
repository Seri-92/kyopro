a = []
for c in input():
    if c == '0' or c == '1':
        a.append(c)
    else:
        if a:
            a.pop()
print("".join(a))
