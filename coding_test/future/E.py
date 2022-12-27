n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

ans = []


if n == 2:
    # 上段左を揃える
    if A[0][1] == B[0][0]:
        ans.append([1, 1, 1])
        A[0] = A[0][::-1]

    elif A[1][0] == B[0][0]:
        ans.append([2, 1, 1])
        A[0][0], A[1][0] = A[1][0], A[0][0]

    elif A[1][1] == B[0][0]:
        ans.append([2, 2, 1])
        A[0][1], A[1][1] = A[1][1], A[0][1]
        ans.append([1, 1, 1])
        A[0] = A[0][::-1]

    # 上段右を揃える
    if A[1][1] == B[0][1]:
        ans.append([2, 2, 1])
        A[0][1], A[1][1] = A[1][1], A[0][0]

    elif A[1][0] == B[0][1]:
        ans.append([1, 2, 1])
        A[1] = A[1][::-1]
        ans.append([2, 2, 1])
        A[0][1], A[1][1] = A[1][1], A[0][1]

    # 下段左を揃える

    if A[1][1] == B[1][0]:
        ans.append([1, 2, 1])

    print('yes')
    print(len(ans))
    for x in ans:
        print(*x)
else:
    print('no')
