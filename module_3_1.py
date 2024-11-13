def count_calls():
  global calls
  calls +=1
  
def  string_info(stroka):
  count_calls()
  # a=len(stroka)
  # b= stroka.upper()
  # c= stroka.lower()
  result=tuple([len(stroka),stroka.upper(), stroka.lower()])
  return result
  
def is_contains(stroka, spisok):
  count_calls()
  lower_stroka = stroka.lower() # приводим строку к общему виду
  copy_spisok=spisok.copy()
  # приведу список к такому же виду, что и строка
  for i in range(len(spisok)):
    copy_spisok[i]=copy_spisok[i].lower()
  # Проверка на вхождение строки в список
  result = lower_stroka in copy_spisok
  return result


calls =0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
