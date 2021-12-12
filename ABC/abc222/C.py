n, m = map(int, input().split())
A = [list(input()) for _ in range(2 * n)]
win = [[0, i] for i in range(2 * n)]
for j in range(m):
    for i in range(n):
        x = win[2*i][1]
        y = win[2*i+1][1]
        x_hand = A[x][j]
        y_hand = A[y][j]
        if x_hand == 'G':
            if y_hand == 'C':
                win[2*i][0] -= 1 
            if y_hand == 'P':
                win[2*i+1][0] -= 1 

        if x_hand == 'C':
            if y_hand == 'P':
                win[2*i][0] -= 1 
            if y_hand == 'G':
                win[2*i+1][0] -= 1 
        if x_hand == 'P':
            if y_hand == 'G':
                win[2*i][0] -= 1 
            if y_hand == 'C':
                win[2*i+1][0] -= 1 
    win.sort()

for i in range(2 * n):
    print(win[i][1] + 1)
        
        