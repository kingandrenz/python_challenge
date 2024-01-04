def find_index(ls: list, n:int):
    """ take a list of int and an int as Arg and return index
        of in of 'n' in the list
    """
    if n not in ls:
        return [n for _ in range(len(ls))]
    else:
        return [i for i in range(len(ls)) if ls[i] == n]


print(find_index( [1, 2, 4, 6, 7, 7], 7))
print(find_index( [1, 2, 4, 6, 7, 7], 8))
