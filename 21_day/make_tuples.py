def make_tuples(lst1: list, lst2: list) -> list:
    """ takes two equal list as Arg, and combine them into 
        a list of tuple.
    """
    tup = [(lst1[i],lst2[i]) for i in range(len(lst1))]

    return tup

print(make_tuples([1,2,3,4], [5,6,7,8]))
