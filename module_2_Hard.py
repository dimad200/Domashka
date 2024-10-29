def search_double(list_,a,b): # Функция для поиска дублей
    c = (a in list_) # Флаг, что a входит в список
    d = (b in list_) # Флаг, что b входит в список
    e= ((c == True) and (d == True))
    if not e:
        list_.append(a)
        list_.append(b)
    if c==True and d==True:
        flag_1 = False # флаг вхождения пары в список
        for i in range(0,len(list_),2):
            if b==list_[i] and a==list_[i+1]:
                flag_1 = True
        if not flag_1:
            list_.append(a)
            list_.append(b)
    return list_


print("Введите выпавшее число")
number = int(input())
list__for_search = []
result = []
# Заполню список для перебора
for i in range(number - 1):
    list__for_search.append(i + 1)
# Заполню список результатами преобразований
for i in range(len(list__for_search)):
    internal_list_ = list__for_search.copy()
    a = internal_list_.pop(i)
    for k in range(len(internal_list_)):
        b = internal_list_[k]
        if number % (a + b) == 0:  #Проверка на соответствие результатов
            search_double(result, a, b)  # поиск дублирующих пар
# Приведу результат к виду, который указан в задании
result_str = ""
#print("result=",result)
for i in range(len(result)):
    result_str = result_str + str(result[i])
print(result_str)
