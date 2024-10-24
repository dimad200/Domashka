first = input("Введи первое число: ")
second = input("Введи второе число: ")
third = input("Введи третье число: ")
if (first == second) and (second == third):
    print("Результат: 3")
elif (first == third) or (second == third) or (first==second):
    print("Результат: 2")
else:
    print("Результат: 0")