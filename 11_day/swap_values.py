def swap_values(lst:list) -> list:
    """ swap the first index with last index """

    lst[0], lst[-1] = lst[-1], lst[0]

    return lst

print(swap_values([2, 4, 67,7]))
