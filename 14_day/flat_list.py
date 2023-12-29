def flat_list(lst: list) -> list:
    """ takes a nested list and return a one dimension list"""
    new_lst = []

    for i in lst:
        for j in i:
            new_lst.append(j)

    return new_lst

print(flat_list([[2,4,5,6]]))
