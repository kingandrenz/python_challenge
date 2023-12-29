def sum_list(lst: list):
    """takes a nested list and return sum of the nested list"""
    my_sum = 0

    for i in lst:
        for j in i:
            my_sum += j

    return my_sum

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
