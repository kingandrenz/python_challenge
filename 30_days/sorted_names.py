def sorted_names(ls:list) -> list:
    """ accept a list of names as argument, return a list 
        with the surname comming first, sorted in alphabetical
        order.
    """
    
    rl = sorted([" ".join(reversed(x.split())) for x in ls])

    return rl
names1 = ["Beyoncé Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]
names = ['Beyonce knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
print(sorted_names(names))

print(sorted_names(names))
