n = list(input())
n_sum = 0
for i in range(len(n)):
    n_sum += int(n[i])
if n_sum % 9 == 0:
    print('Yes')
else:
    print('No')