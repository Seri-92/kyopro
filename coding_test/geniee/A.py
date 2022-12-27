import csv
import math
thi_list = []
alt_list = []
with open('input.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        city, a, t, h = row
        alt_list.append(a)
        thi = 0.81 * t + 0.01 * h * (0.99 * t - 14.3) + 46.3
        thi_list.append(thi)
n = len(thi_list)
thi_mean = sum(thi_list) / n
alt_mean = sum(alt_list) / n


s_thi_alt = 0
for i in range(n):
    s_thi_alt += (thi_list[i] - thi_mean) * (alt_list[i] - alt_mean)

s_thi_alt /= n

s_thi = 0
for i in range(n):
    s_thi += (thi_list[i] - thi_mean) ** 2
s_thi /= n
s_thi = math.sqrt(s_thi)

s_alt = 0
for i in range(n):
    s_alt += (alt_list[i] - alt_mean) ** 2
s_alt /= n
s_alt = math.sqrt(s_alt)

r = s_thi_alt / s_thi / s_alt

print(r)
