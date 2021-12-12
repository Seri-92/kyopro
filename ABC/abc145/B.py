n = int(input())
s = input()
print('Yes' if s[:n//2] * 2 == s else 'No')