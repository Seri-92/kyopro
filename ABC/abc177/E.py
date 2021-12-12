import math
n = int(input())
A = list(map(int, input().split())) 

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

data = get_sieve_of_eratosthenes(10**6)

a = 1
for j in range(n):
    a *= A[j]

flag_1 = True
for k in data:
    if a % k**2 == 0:
        flag_1 = False
if flag_1:
    print('pairwise coprime')
    exit()

flag_2 = True
for l in data:
    for m in A:
        