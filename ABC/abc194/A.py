a, b = map(int, input().split())
if a + b >= 15 and b >= 8:ans = 1
elif a + b >= 10 and b >= 3:ans = 2
elif a + b >= 3:ans = 3
else:ans = 4

print(ans)
