import re


def calculate_structure_sum(data_structure):
    data = str(list(data_structure))
    data = re.findall('\w+', data)
    new_data = []
    for i in range(len(data)):
        if data[i].isdigit():
            data[i] = int(data[i])
            new_data.append(data[i])
        else:
            new_data.append(len(data[i]))
    print(data)
    print(new_data)
    return sum(new_data)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
