n = int(input())
section_list = [list(map(int, input().split())) for _ in range(n)]

def section_min_max(l):
    if l[0] in {1, 2}:
        section_min = l[1] 
    else:
        section_min = l[1] + 0.1
    if l[0] in {1, 3}:
        section_max = l[2]
    else:
        section_max = l[2] - 0.1
    if section_max < section_min:
        return -1, -1
    return section_min, section_max

ans = 0
for i in range(n):
    x_min, x_max = section_min_max(section_list[i])
    if x_min == -1:
        continue
    for j in range(i+1, n):
        y_min, y_max = section_min_max(section_list[j])
        if y_min == -1:
            continue
        if x_min > y_max or y_min > x_max:
            continue
        ans += 1

print(ans)
