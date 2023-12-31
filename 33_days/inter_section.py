def inter_section(ls1:list, ls2:list) -> list:
    """ returns the elements that are both present in list1 and
        list2
    """
    return tuple([x for x in ls1 if x in ls2])

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))
