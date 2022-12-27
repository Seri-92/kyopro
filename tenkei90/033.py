h, w = map(int, input().split())

def judge(light_array):
    for i in range(h-1):
        for j in range(w-1):
            x = (
                light_array[i][j] + light_array[i+1][j] + light_array[i][j+1]
                + light_array[i+1][j+1]
                )
            if x >= 2:
                return False

    return sum(sum(light_array[i]) for i in range(h))

ans = 0
for i in range(1<<(h*w)):
    light_array =[[0] * w for _ in range(h)] 
    for j in range(h*w):
        if i >> j & 1:
            light_array[(j//w)][j%w] = 1
    ans = max(ans, judge(light_array))

print(ans)
    
