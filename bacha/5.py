a, b, c, k = map(int, input().split())
lst = [a, b, c]

for i in range(k):
    lst_now = lst[:]
    a = sum(lst_now) - lst_now[0]
    b = sum(lst_now) - lst_now[1]
    c = sum(lst_now) - lst_now[2]
    lst = [a, b, c]

if abs(a - b) > 10 ** 18:
    print('Unfair')
    exit()
print(a - b)