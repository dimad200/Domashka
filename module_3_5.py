# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(number=0):
  if int(number)==0:
    return  0

  str_number = str(number)
  first=int(str_number[0])

  if len(str_number)<2 or int(str_number[1:])==0:
  # если число больше не перебрать, или остались только нули вернем первую цифру
    return first
  else:
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(100000)

print(result)

# Вывод на консоль:
# 24