def prime_factorize(n):
    list_ = []
    i = 2
    m = n
    while i ** 2 <= m:
        while n % i == 0:
            n //= i
            list_.append(i)
        i += 1
    if n != 1:
        list_.append(n)
    return list_
print(prime_factorize(int(input())))            
