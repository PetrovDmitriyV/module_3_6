def calculate_structure_sum(data_structure):
    a = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    n = 0
    m = 0
    z = 0
    sums = data_structure
    for key in sums:
        # print(key)
        for p in range(len(key)):
            z = a1 + a2 + a3 + a4 + a5      # 6 11 5 29 48
            if isinstance(key, list) == True:  # [1, 2, 3]
                for i in key:
                    m = m + i
                a1 = m      # a1 = 6
                break
            if isinstance(key, dict) == True:  # {'a': 4, 'b': 5}
                b = key
                for key, value in b.items():
                    n = n + len(key) + value
                a2 = n      # 11
                break
            if isinstance(key, str) == True:  # Hello
                a3 = + len(key)     # a3 = 5
                break

            if isinstance(key, tuple) == True:  # (6, {'cube': 7, 'drum': 8}) ((), [{(2, 'Urban', ('Urban2', 35))}])
                c = key
                for key in c:
                    if isinstance(key, int) == True:    # 6
                        m = key       # a4 = 6

                    if isinstance(key, dict) == True:   # 23 = {'cube': 7, 'drum': 8}
                        d = key
                        for key, value in d.items():
                            m = m + len(key) + value
                        a4 = m      # a4 = 29 = 6 + 23
                        break
                    if isinstance(key, list) == True:  # [{(2, 'Urban', ('Urban2', 35))}]
                        result1 = []
                        e = key
                        e = list(*e)
                        e = tuple(*e)  # (2, 'Urban', ('Urban2', 35))
                        for key in e:
                            if isinstance(key, int) == True:
                                a = key         # a = 2
                            if isinstance(key, str) == True:
                                a = a + len(key)        # a = 2 + Urban
                            if isinstance(key, tuple) == True:
                                f = list(key)
                                f = tuple(f)        # ('Urban2', 35)
                                for key in f:
                                    if isinstance(key, int) == True:
                                        a = key     # 35
                                        result1.append(a)
                                    if isinstance(key, str) == True:
                                        a = a + len(key)    # 13 = (2 + Urban + Urban2)
                                        result1.append(a)
                        a5 = sum(result1)  # a5 = 48
                        break


    return z

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
