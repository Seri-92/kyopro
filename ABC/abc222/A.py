n = input()
l = len(n)
if l < 4:
    n = '0' * (4 - l) + n
print(n)
