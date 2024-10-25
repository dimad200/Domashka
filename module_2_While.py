my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
dlinna_spiska = len(my_list)
indeks = 0
while dlinna_spiska > indeks:
    if my_list[indeks] > 0:
        print(my_list[indeks])
    elif my_list[indeks] == 0:
        indeks = indeks + 1
        continue
    else:
        break
    indeks = indeks + 1
