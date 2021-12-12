k = int(input())
if k 
n = 1
while True:
    seven_number = 0
    for i in range(n):
        seven_number += 7 * 10 ** i
    if seven_number % k == 0:
        print(n)
        break
    n += 1
