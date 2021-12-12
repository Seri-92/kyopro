from itertools import permutations 
n = int(input())
p = list(map(int, input().split())) 
q = list(map(int, input().split()))
 
i = 0
for x in permutations(range(1, n+1)):
    i += 1
    if list(x) == p:
        a = i
    if list(x) == q:
        b = i

print(abs(a-b))