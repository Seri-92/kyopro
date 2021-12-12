s = input()
p = s.index("A")
q = s[::-1].index("Z")
print(len(s)-q-p)