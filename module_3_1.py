def count_calls():
    global calls
    calls +=1

def  string_info(stroka):
    a=len(stroka)
    b= stroka.upper()
    c= stroka.lower()
    result=tuple([len(stroka),stroka.upper(), stroka.lower()])
    return result

print(string_info(input()))