def zeroed(my_list:list):
    """ take a list od number ans zero(0) the first and last index"""
    my_list[0], my_list[-1] = 0, 0
    return my_list

lst =  [2, 5, 7, 8, 9]
print(zeroed(lst))
