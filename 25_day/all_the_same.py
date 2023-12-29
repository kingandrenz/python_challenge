from typing import Union

def all_the_same(st:Union[str, tuple, list]):
    """ takes one argument (string/list/tuple) and check if all
        the elements are the same.
    """
    return all(i == st[0] for i in st)

print(all_the_same(["Mary", "Mary", "Mary"])) 
