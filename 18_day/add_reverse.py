def add_reverse(lst1: list, lst2: list) -> list:
    """ param1: list, param2: list, add param1 +
        param2, and return reverse of the result.
    """
    new_lst = []
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            new_lst.append(lst1[i] + lst2[i])
            new_lst.reverse()
        return new_lst
    else:
        return f"The list are not of equal length."

print(add_reverse([10, 12, 34],  [12, 56, 78]))
