def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if str('@') not in recipient or str('@') not in sender:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    correct_domen = ['.ru', '.net', '.com']
    for i in correct_domen:
        if i in recipient:
            break
        elif i not in recipient and i == '.com':
            return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    for i in correct_domen:
        if i in sender:
            break
        elif i not in sender and i == '.com':
            return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        return print('Нельзя отправить письмо самому себе!')
    elif sender != "university.help@gmail.com":
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

send_email('1', '1@mail.ru')
send_email('12', '12@mail.ru', sender='12@gmail.com')
send_email('123', '123@mail.ru', sender='123@mail.ur')
send_email('1234', 'university.help@gmail.com')
