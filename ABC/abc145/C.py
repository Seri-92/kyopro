from itertools import permutations
import math
n = int(input())
dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))

ans = 0

for v in permutations(dots):
    for i in range(n-1):
        ans += math.sqrt((v[i][0] - v[i+1][0])**2\
            + (v[i][1] - v[i+1][1])**2)

ans /= math.factorial(n)
print(ans)