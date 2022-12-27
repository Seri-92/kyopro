n = int(input())
name_list = [input().split() for _ in range(n)]

for i in range(n):
    s, t = name_list[i]
    s_flag = True
    t_flag = True

    for j in range(n):
        if i == j:
            continue
        ss, tt = name_list[j]
        if s == ss or s == tt:
            s_flag = False
        if t == ss or t == tt:
            t_flag = False
    if s_flag or t_flag:
        continue
    else:
        print('No')
        exit()

print('Yes')


