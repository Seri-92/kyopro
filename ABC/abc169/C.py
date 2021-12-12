from decimal import Decimal 
a, b = map(Decimal, input().split())
ans = a * b // 1
print(ans)