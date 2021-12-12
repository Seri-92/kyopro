n = int(input())
S = []
for i in range(n):
    S.append(input())

lst = [S.count('AC'), S.count('WA'), S.count('TLE'),
S.count('RE')]
 
print('AC x ' + str(lst[0]))
print('WA x ' + str(lst[1]))
print('TLE x ' + str(lst[2]))
print('RE x ' + str(lst[3]))




