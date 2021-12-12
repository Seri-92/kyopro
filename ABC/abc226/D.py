import math
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
s = set()
for i in range(n-1):
    for j in range(i+1, n):
        maho_x, maho_y = a[i][0]-a[j][0], a[i][1]-a[j][1]
        g = math.gcd(maho_x, maho_y)
        s.add((maho_x // g, maho_y // g))
        s.add((- maho_x // g, - maho_y // g))

print(len(s))
        
