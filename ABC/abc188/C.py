n = int(input())
A = list(map(int, input().split()))

winner_list = []
for i, a in enumerate(A):
    winner_list.append([i+1, a])

def judge_winners(winner_list):
    l = len(winner_list)
    winner_list_tmp = []
    for i in range(l//2):
        x = winner_list[2*i]
        y = winner_list[2*i+1]
        if x[1] > y[1]:
            winner_list_tmp.append(x)
        else:
            winner_list_tmp.append(y)
    return winner_list_tmp

while len(winner_list) > 2:
    winner_list = judge_winners(winner_list)
    
x, y = winner_list
if x[1] > y[1]:
    ans = y[0]
else:
    ans = x[0]

print(ans)
