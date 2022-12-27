year = 2007
month = 1
youbi = 0 # 金曜

cnt = 1
l = []
while True:
    if month in {4, 6, 9, 11}:
        youbi += 30
        youbi %= 7
    elif month == 2:
        if year % 4 == 0:
            youbi += 29
            youbi %= 7
        else:
            youbi += 28
            youbi %= 7
    else:
        youbi += 31
        youbi %= 7
    month += 1
    if month == 13:
        month = 1
        year += 1
    if youbi == 0:
        cnt += 1
        l.append((year, month))
    if cnt == 666:
        print(year, month)
        break
print(l[:4])
