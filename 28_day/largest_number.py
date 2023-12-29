def largest_number(ls: list):
    """ take a list of integers as argument and return a
        an integer rearrange from the list from the greatest
        to the lowest
    """
    a = ''.join(str(i) for i in ls)
    b = sorted(a, reverse = True)
    b = int("".join(i for i in b))

    return "{:,}".format(b)

list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))

