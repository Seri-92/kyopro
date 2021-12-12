S = set()
for i in range(3):
    S.add(input())

A = {'ABC', 'ARC', 'AGC', 'AHC'} 

print(list(A-S)[0])
