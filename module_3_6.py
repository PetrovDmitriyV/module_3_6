def calculate_structure_sum(data_structure):
    data = []
    for v in range(len(data_structure)):
        def sums(*args):
            if isinstance(*args, list):
                for key in data_structure[v]:
                    if isinstance(key, int):
                        data.append(key)
                    if isinstance(key, str):
                        data.append(len(key))
            if isinstance(*args, dict):
                for key, value in data_structure[v].items():
                    data.append(len(key))
                    data.append(value)
            if isinstance(*args, str):
                data.append(len(data_structure[v]))
            if isinstance(*args, tuple):
                x, y = data_structure[v]
                if isinstance(x, int):
                    data.append(x)
                if isinstance(y, dict):
                    for key, value in y.items():
                        data.append(len(key))
                        data.append(value)
                if isinstance(y, list):
                    for key in y:
                        if isinstance(key, int):
                            data.append(key)
                        if isinstance(key, str):
                            data.append(len(key))
                        if isinstance(key, set):
                            key_list = list(*key)
                            if isinstance(key_list, list):
                                for key in key_list:
                                    if isinstance(key, int):
                                        data.append(key)
                                    if isinstance(key, str):
                                        data.append(len(key))
                                    if isinstance(key, tuple):
                                        key_tuple = list(key)
                                        if isinstance(key_tuple, list):
                                            for key in key_tuple:
                                                if isinstance(key, int):
                                                    data.append(key)
                                                if isinstance(key, str):
                                                    data.append(len(key))
        sums(data_structure[v])
    print(data_structure)
    print(data)
    return sum(data)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = calculate_structure_sum(data_structure)
print(result)
