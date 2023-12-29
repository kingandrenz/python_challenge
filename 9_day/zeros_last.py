def zeros_last(lst:list) -> list:
    """ takes in a list check if a list has zero and 
        move it to the back of the list
    """

    if not any(element != 0 for element in lst):
        return sorted(lst, reverse=False)
    else:
        for i in lst:
            if i == 0:
                lst.append(lst.pop(lst.index(0)))
        return lst

print(zeros_last([1, 4, 6, 0, 7, 0, 9]))
print(zeros_last([2, 1, 4, 7, 6]))
