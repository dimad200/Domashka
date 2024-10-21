grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# создам отсортированный по алфавиту список студентов:
sorted_students=sorted(students)
# создам список с средними оценками:
Sredniy_bal=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4]),]
print(Sredniy_bal)
#Создам итоговый словарь:
Itog={sorted_students[0]:Sredniy_bal[0],sorted_students[1]:Sredniy_bal[1],sorted_students[2]:Sredniy_bal[2],sorted_students[3]:Sredniy_bal[3],sorted_students[4]:Sredniy_bal[4]}
print(Itog)