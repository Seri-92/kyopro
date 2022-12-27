inverse_sum = 0
n = 1
while True:
    inverse_sum += 1 / n
    if inverse_sum > 15:
        break
    n += 1
print(n)
