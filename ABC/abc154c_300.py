N = int(input())
A_list = list(map(int, input().split()))
A_set = set(A_list)
if len(A_list) == len(A_set):
    print("YES")
else:
    print("NO")