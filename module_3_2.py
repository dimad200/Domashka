# Функция отправки письма
def send_email(message, recipient, sender="university.help@gmail.com"):
    # Установка флага собаки
    if not ("@" in recipient and "@" in sender):
        flag_sobaka = False
    else:
        flag_sobaka = True
    # Установка флага корректного получателя
    if recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net"):
        flag_recipient = True
    else:
         flag_recipient = False
    # Установка флага корректного отправителя
    if sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net"):
        flag_sender = True
    else:
        flag_sender = False

    # Проверка, что все поля заполнены (флаги подняты)
    if flag_sobaka and flag_recipient and flag_sender:
        # Проверяме что шлем самому себе
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    # print(flag_sobaka, flag_recipient, flag_sender)



# Собственно сама программа
#Тесты из задания
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

message = 'Вы видите это сообщение как лучший студент курса!'
sender = 'urban.info@gmail.com'
recipient = 'urban.fan@mail.ru'
send_email(message, recipient, sender)
