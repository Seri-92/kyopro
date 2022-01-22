def dfs(A):
    if len(A) == 3:
        print(f'{A=}')
        return

    for v in range(3):
        A.append(v)
        print(A)
        dfs(A)
        A.pop()
dfs([])
