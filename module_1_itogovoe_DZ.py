from urllib.parse import ResultBase

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# создам отсортированный по алфавиту список студентов:
sorted_students=sorted(students)
# создам список с средними оценками:
GPA=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4]),]
#Создам итоговый словарь:
Result={sorted_students[0]:GPA[0],sorted_students[1]:GPA[1],sorted_students[2]:GPA[2],sorted_students[3]:GPA[3],sorted_students[4]:GPA[4]}
#Вывод словаря
print(Result)