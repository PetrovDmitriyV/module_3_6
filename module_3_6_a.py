data = []


def calculate_structure_sum(data_structure):
    global data

    def sum_list(args):  # Расчет суммы в type(list)
        for key in args:
            if isinstance(key, int):
                data.append(key)
            if isinstance(key, str):
                data.append(len(key))
            if isinstance(key, tuple):
                key = list(key)
                sum_list(key)
            if isinstance(key, set):
                key = list(*key)
                sum_list(key)

        return data

    def sum_dict(args):  # Расчет суммы в type(dict)
        for key, value in args.items():
            data.append(len(key))
            data.append(value)

        return data

    def sum_str(args):  # Расчет суммы в type(str)
        data.append(len(args))

        return data

    def sum_int(args):  # Расчет суммы в type(int)
        data.append(args)

        return data

    def sum_tuple(args):  # Расчет суммы в type(tuple)
        for key in args:
            if isinstance(key, list):
                sum_list(key)
            if isinstance(key, dict):
                sum_dict(key)
            if isinstance(key, str):
                sum_str(key)
            if isinstance(key, int):
                sum_int(key)

    if len(data_structure) == 0:
        return print(f'Конец расчета функции: {sum(data)}')  # Результат
    else:
        for v in range(len(data_structure)):
            if isinstance(data_structure[v], list):  # Если элемент list, то запускаем функцию расчета для list
                sum_list(data_structure[v])

            if isinstance(data_structure[v], dict):  # Если элемент dict, то запускаем функцию расчета для dict
                sum_dict(data_structure[v])

            if isinstance(data_structure[v], str):  # Если элемент str, то запускаем функцию расчета для str
                sum_str(data_structure[v])

            if isinstance(data_structure[v], tuple):  # Если элемент tuple, то запускаем функцию расчета для tuple
                sum_tuple(data_structure[v])

            if isinstance(data_structure[v], int):  # Если элемент int, то запускаем функцию расчета для int
                sum_int(data_structure[v])
            print(f'Обработан элемент: {data_structure[v]}\n Добавлено в результат: {data}\n Cумма = {sum(data)}')
            del data_structure[v]  # Удаляем обработанный элемент

            return calculate_structure_sum(data_structure)  # Запускаем заново расчет без обработанного элемента

    return data


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = calculate_structure_sum(data_structure)
