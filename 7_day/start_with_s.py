def start_with_s(lst:list):
    """return a dictionary of name that start with 'S' 
        with name as key and number of time it apper as value
    """
    set_name = sorted(set(lst))
    s_name = {}

    for i in set_name:
        if i[0] == 'S':
            s_name[i] = lst.count(i)

    return s_name

names = ["Joseph","Nathan", "Siasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

#Or we can use :

"""
def start_with_s(lst:list):
    s_dict = {}

    for i in lst:
        if i startWith('S'):
            s_dict.update({i: s_dict.count(i)})
    return s_dict
"""
print(start_with_s(names))
