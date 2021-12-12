n, k = map(int, input().split())
sum_p = []
for i in range(n):
    Points = list(map(int, input().split()))
    sum_p.append(sum(Points))
sorted_sum_p = sorted(sum_p, reverse=True)
for i in range(n):
    if sum_p[i] + 300 >= sorted_sum_p[k-1]:
        print('Yes')
    else:
        print('No')
    