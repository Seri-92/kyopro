from heapq import heapify, heappush, heappop

n, k = map(int, input().split())
A = list(map(lambda x: - int(x), input().split()))


heapify(A)
print(A)
print(heappop(A))
print(heappop(A))


