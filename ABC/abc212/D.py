from heapq import heappush, heappop
n = int(input())
h = []
add_num = 0

for i in range(n):
    query = list(map(int, input().split()))
    if len(query) == 2:
        p, x = query[0], query[1]
        if p == 2:
            add_num += x
        elif p == 1:
            heappush(h, x - add_num)
    else:
        print(heappop(h) + add_num)

