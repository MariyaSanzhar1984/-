my_lest = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_lest): #чтобы не выйти за границу списка, сравнение текущего индекса  и длины списка
    if my_lest[index] < 0: # перебор списка положительных
        break
    elif my_lest[index] == 0:
        index += 1
        continue
    print(my_lest [index])
    index += 1