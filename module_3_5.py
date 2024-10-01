def get_multiplied_digits(number):
    str_number = str(number)
    for i in str_number:
        if i == '0':
            str_number = str_number.replace('0', '')
            break
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits('00000102400000')
print(result)
