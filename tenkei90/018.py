import math
T = int(input())
l, X, Y = map(int, input().split())
q = int(input())
E = [int(input()) for _ in range(q)]

def coordinate(t):
    y = -l / 2 * math.sin(2 * math.pi * t / T)
    z = l / 2 * (1 - math.cos(2 * math.pi * t /T))
    x = 0
    return [x, y, z]

def angle(t):
    x, y, z = coordinate(t)
    height = z
    v_dist = math.dist([x, y], [X, Y])
    return math.degrees(math.atan(height / v_dist))

for t in E:
    print(angle(t))


