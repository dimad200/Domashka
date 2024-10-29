def Search_duble(list,a,b): # Функция для поиска дублей
    c = (a in list) # Флаг, что a входит в список
    d = (b in list) # Флаг, что b входит в список
    e=((c==True) and (d==True))
    if (e==False):
        list.append(a)
        list.append(b)
    if c==True and d==True:
        Flag_1=False
        for i in range(0,len(list),2):
            if b==list[i] and a==list[i+1]:
                Flag_1=True
        if Flag_1==False:
            list.append(a)
            list.append(b)

    return list


print("Введите выпавшее число")
number = int(input())
List_for_search = []
result = []
# Заполню список для перебора
for i in range(number - 1):
    List_for_search.append(i + 1)
# Заполню список результами преобразований 
for i in range(len(List_for_search)):
    internal_list = List_for_search.copy()
    a = internal_list.pop(i)
    for k in range(len(internal_list)):
        b = internal_list[k]
        if number % (a + b) == 0:  #Проверка на соответствие результатов
            Search_duble(result, a, b)  # поиск дублирующих пар
# Приведу результат к виду, который указан в задании
result_str = ""
#print("result=",result)
for i in range(len(result)):
    result_str = result_str + str(result[i])
print(result_str)
