n, k = map(int, input().split())
get_money = 0
friends = []
for _ in range(n):
    friends.append(list(map(int, input().split())))

friends.sort()

for i in range(n):
    if k + get_money >= friends[i][0]:
        get_money += friends[i][1]
    else:
        break

print(k + get_money)

