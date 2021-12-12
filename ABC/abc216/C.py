n = int(input())
ans = []
for i in range(120):
    if n < 1:
        break
    elif n % 2 == 1:
        n -= 1
        ans.append('A')
    else: 
        n //= 2
        ans.append('B')

ans = ''.join(reversed(ans))
print(ans)