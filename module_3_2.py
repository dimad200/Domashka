def  send_email(message,recipient,sender = "university.help@gmail.com"):
    # Установка флага собаки
    if  not("@" in recipient and "@" in sender):
        flag_sobaka=False
    else:
         flag_sobaka=True
    # Установка флага корректного получателя
    if right_ending(".com",recipient) or right_ending(".ru",recipient) or right_ending(".net",recipient):
         flag_recipient=True
    else:
         flag_recipient=False
    # Установка флага корректного отправителя
    if right_ending(".com", sender) or right_ending(".ru", sender) or right_ending(".net", sender):
        flag_sender = True
    else:
        flag_sender = False

    # Остаток программы
    if flag_sobaka and flag_recipient and flag_sender:
        # Проверяме что шлем самому себе
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")





    print(flag_sobaka,flag_recipient,flag_sender)
# функция, которая проверит, что кончается на заданную последовательность

def right_ending(what_looking, where_looking):
    flag=False
    for i in range(len(what_looking)):
         if what_looking[-1-i] == where_looking[-1-i]:
             flag = True
         else:
             flag = False
             break
    return flag






send_email("rjn yf j,jhjl","vasya@pupkin.ru",sender = "1university.help@gmail.com")
print(right_ending("qwerty", "123456qwerty"))
