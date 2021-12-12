P = list(map(int, input().split()))
s = ''
for p in P:
    s += chr(ord('a') + p - 1)
print(s) 
   
