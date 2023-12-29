def difference(a: list, b:list) -> list:
    """
        arg1: list

        arg2: list

        return: elem in a not in b and elem in b not in a

    """

    uniq_a = [x for x in a if x not in b ]
    uniq_b = [x for x in b if x not in a ]

    return uniq_a + uniq_b

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

print(difference(list1, list2))
