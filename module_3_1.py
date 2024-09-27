from operator import index

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_ = len(string)
    upper_ = (string).upper()
    lower_ = (string).lower()
    return (len_, upper_, lower_)


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return (True)
        else:
            continue
    return (False)


print(string_info('Как же я устал работать на трёх работах'))
print(string_info('Но я люблю свою работу'))
print(is_contains('ТрУдОвЫебуДнИ', ['задолбыш', 'ТрудоВыебудни', '']))
print(is_contains('куда', ['Кудах', 'Тудах']))
print(calls)
