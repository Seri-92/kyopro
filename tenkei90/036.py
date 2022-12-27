n, q = map(int, input().split())
coordinate_list = [list(map(int, input().split())) for _ in range(n)]
query_list = [int(input()) - 1 for _ in range(q)]

sum_list = []
difference_list = []
for i in range(n):
    x, y = coordinate_list[i]
    sum_list.append(x+y)
    difference_list.append(x-y)

sum_list.sort()
difference_list.sort()

for i in query_list:
    x, y = coordinate_list[i]
    ans = max(
            abs(sum_list[0] - (x+y)), abs(sum_list[-1] - (x+y)),
            abs(difference_list[0] - (x-y)), abs(difference_list[-1] - (x-y))
            )
    
    print(ans)

