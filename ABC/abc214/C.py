n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

T_sorted = []
for i in range(len(T)):
    T_sorted.append((T[i],i)) 
    
T_sorted.sort()

time_min = [10**8 * 11] * n
start = T_sorted[0][1]
time_min[start] = T_sorted[0][0]
for i in range(n):
    crr = (start + i) % n
    nxt = (crr + 1) % n
    time_min[nxt] = min(time_min[nxt], time_min[crr]+S[crr], T[nxt]) 
for x in time_min:
    print(x)
    
    
    
