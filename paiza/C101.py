x = input()
cnt = 0
for i in range(365):
    if x in str(i):
        cnt += 1
print(cnt)
