def biggest_odd(n:str):
    """ takes a string of numbers and return the biggest
        odd number in the list
    """
    lst = []
    b_odd = max([int(x) for x in n if int(x) % 2 != 0])

    

    return (b_odd)
my_s = "23569"
print(biggest_odd(my_s))
