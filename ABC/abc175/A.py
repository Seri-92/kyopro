s = input()
if s == 'SSS':
    ans = 0
elif s == 'RRR':
    ans = 3
elif s in ['RRS', 'SRR']:
    ans = 2
else:
    ans = 1
print(ans)