my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
leight = len(my_list)
while index != leight:
    if my_list[index] != 0 and my_list[index] > 0:
        print(my_list[index])
        index += 1
    elif my_list[index] == 0:
        index += 1
        continue
    elif my_list[index] < 0:
        break