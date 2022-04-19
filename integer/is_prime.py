def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input())    
print('YES' if isPrime(n) else 'NO')
        
