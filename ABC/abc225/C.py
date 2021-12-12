n, m = map(int, input().split())
B = list(map(int, input().split()))
start = B[0]
if m > 1:
    if start % 7 == 0:
        print('No')
        exit()
start_min_mod = 7 - m + 1
if start % 7 > start_min_mod:
    print('No')
    exit()
if B != list(range(start, start + m)):
    print('No')
    exit()

for i in range(1, n):
    C = list(map(int, input().split()))
    if C != list(range(start + i * 7, start + i * 7 + m)):
        print('No')
        exit()
print('Yes')