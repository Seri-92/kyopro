import math
a, b, h, m = map(int, input().split())
theta  = (h * 60 + m) * 11 / 2
c_square = a ** 2 +  b ** 2 - 2 * a * b * math.cos(math.radians(theta))
c = math.sqrt(c_square)
print(c)