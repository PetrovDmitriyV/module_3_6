def calculate_structure_sum(data_structure):
    a = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    sums = data_structure
    for key in sums:
        # print(key)
        for p in range(len(key)):
            a = a1 + a2 + a3 + a4
            if isinstance(key, list) == True:
                for i in key:
                    a = a + i
                a1 = a
                break
            if isinstance(key, str) == True:
                a = a + len(key)
                a2 = a
                break
            if isinstance(key, dict) == True:
                b = key
                for key, value in b.items():
                    a = a + len(key) + value
                a3 = a
                break
            if isinstance(key, tuple) == True:
                c = key
                for key in c:
                    if isinstance(key, int) == True:
                        a = key
                        break
                    if isinstance(key, dict) == True:
                        d = key
                        for key, value in d.items():
                            a = a + len(key) + value
                        break
                    if isinstance(key, list) == True:
                        result1 = []
                        e = key
                        e = list(*e)
                        e = tuple(*e)
                        for key in e:
                            if isinstance(key, int) == True:
                                a = key
                            if isinstance(key, str) == True:
                                a = a + len(key)
                            if isinstance(key, tuple) == True:
                                f = list(key)
                                f = tuple(f)
                                for key in f:
                                    if isinstance(key, int) == True:
                                        a = key
                                        result1.append(a)
                                    if isinstance(key, str) == True:
                                        a = a + len(key)
                                        result1.append(a)
                        a4 = sum(result1)
                        break
    return  a


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
