def calculate_structure_sum(args):
    total = 0
    if isinstance(args, int):
        return args
    elif isinstance(args, str):
        return len(args)
    elif isinstance(args, dict):
        for key, value in args.items():
            if isinstance(key, str):
                total += len(key)
            elif isinstance(key, int):
                total += key
            total += calculate_structure_sum(value)
    elif isinstance(args, (list, tuple, set)):
        for i in args:
            total += calculate_structure_sum(i)
    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)