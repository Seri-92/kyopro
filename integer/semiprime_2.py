def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_semiprime(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            if is_prime(i) and is_prime(n//i):
                return True
        i += 1
    return False


for i in range(1100):
    if is_semiprime(i):
        if i == 1027:
            print(str(i) + ' <- 優希の誕生日')
        else:
            print(i)


