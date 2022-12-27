l = [1, 0, 5]

for i in range(28):
    l.append(l[-1] + l[-2] + l[-3])

print(len(l))
print(l[-1])

