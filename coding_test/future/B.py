coord_list = list(map(int, input().split()))
rect_1_x = []
rect_1_y = []
for i in range(8):
    if i % 2 == 0:
        rect_1_x.append(coord_list[i])
    else:
        rect_1_y.append(coord_list[i])

rect_2_x = []
rect_2_y = []
for i in range(8, 16):
    if i % 2 == 0:
        rect_2_x.append(coord_list[i])
    else:
        rect_2_y.append(coord_list[i])

external_flag = False
if max(rect_1_x) < min(rect_2_x):
    external_flag = True
elif max(rect_2_x) < min(rect_1_x):
    external_flag = True

if max(rect_1_y) < min(rect_2_y):
    external_flag = True
elif max(rect_2_y) < min(rect_1_y):
    external_flag = True


# rect2 in rect1
inner_flag_1 = True
if not(min(rect_1_x) < min(rect_2_x) < max(rect_2_x) < max(rect_1_x)):
    inner_flag_1 = False
if not(min(rect_1_y) < min(rect_2_y) < max(rect_2_y) < max(rect_1_y)):
    inner_flag_1 = False

# rect1 in rect2
inner_flag_2 = True
if not(min(rect_2_x) < min(rect_1_x) < max(rect_1_x) < max(rect_2_x)):
    inner_flag_2 = False
if not(min(rect_2_y) < min(rect_1_y) < max(rect_1_y) < max(rect_2_y)):
    inner_flag_2 = False

if inner_flag_1 or inner_flag_2:
    inner_flag = True
else:
    inner_flag = False


if external_flag or inner_flag:
    print('FALSE')
else:
    print('TRUE')
