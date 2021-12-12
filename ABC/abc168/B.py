k = int(input())
s = input()
if len(s) <= k:
    print(s)
else:
    s = s[:k] + '...'
    print(s)