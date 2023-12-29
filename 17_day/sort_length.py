def sort_length(lst: list) -> list:
    """ takes a list as argument and return a sorted
        a sorted string in the list 
    """
    for i in range(0, len(lst) - 1):
        if len(lst[i]) > len(lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
print(sort_length(['Peter', 'Jon', 'Andrew'])) 
