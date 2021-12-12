for i in range(1, 101):
    a = (101 * i) / (101 - i)
    if a.is_integer():
        print(a, i)
        print('------')
