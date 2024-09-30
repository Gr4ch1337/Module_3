def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('строка', 1, False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['список', 1, True]
values_dict = {'a': 'словарь', 'b': 2, 'c': False}

values_list_2 = [1123, 1.5]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
