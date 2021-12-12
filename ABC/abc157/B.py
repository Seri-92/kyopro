A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))
A_3 = list(map(int, input().split()))

N = int(input())
for i in range(N):
    b = int(input())
    if A_1[0] == b:
        A_1[0] = 0
    if A_1[1] == b:
        A_1[1] = 0
    if A_1[2] == b:
        A_1[2] = 0
    if A_2[0] == b:
        A_2[0] = 0
    if A_2[1] == b:
        A_2[1] = 0
    if A_2[2] == b:
        A_2[2] = 0
    if A_3[0] == b:
        A_3[0] = 0
    if A_3[1] == b:
        A_3[1] = 0
    if A_3[2] == b:
        A_3[2] = 0
if A_1 == [0, 0, 0] or A_2 == [0, 0, 0] or A_3 == [0, 0, 0]:
    print("Yes")
    exit()
for j in range(3):
     if A_1[j] == 0 and A_2[j] == 0 and A_3[j] == 0:
         print("Yes")
         exit()
if A_1[0] == 0 and A_2[1] == 0 and A_3[2] == 0:
    print("Yes")
    exit()

if A_3[0] == 0 and A_2[1] == 0 and A_1[2] == 0:
    print("Yes")
    exit()

print("No")