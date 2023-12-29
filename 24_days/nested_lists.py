def nested_lists(*args:list) -> list:
    """ Takes any number of list and returns a two dimentional
        list.
    """
    two_dm = [x for x in args]
    return two_dm

print(nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))
