def odd_even(lst:list):
    """ returns the difference between large even
        number and smallest odd numnber
    """
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]

    return f"{max(even)} - {min(odd)} = {max(even) - min(odd)}"

lst1 = [1, 2, 4, 6]

print (odd_even(lst1))
