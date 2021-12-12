n = input()
for i in range(10):
    n_tmp = '0' * i + n
    if n_tmp == n_tmp[::-1]:
        print('Yes')
        exit()
print('No')