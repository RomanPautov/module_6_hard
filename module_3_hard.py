data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
total_sum = 0

def calculate_structure_sum(data):
    global total_sum

    if isinstance(data, int):
        total_sum += data

    elif isinstance(data, str):
        total_sum += len(data)

    elif isinstance(data, (list, tuple, set)):
        for i in data:
            calculate_structure_sum(i)
    elif isinstance(data, dict):
        for key, value in data.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)

    return total_sum


result = 'сумма всех чисел и длин всех строк равна:', calculate_structure_sum(data_structure)

print(*result)