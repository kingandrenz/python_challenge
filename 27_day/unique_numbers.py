def unique_numbers(ls: list) -> list:
    """
        arg: list of numbers
        return: 
            originalist: if the diff btwn the sum of the list &
                        sum of the unique numbers in the list is
                        even, else;
            list_with_unique_numbers:
    """

    unique_lst = [x for x in set(ls)]

    if (sum(ls) - sum(unique_lst)) % 2 == 0:
        return ls
    else: 
        return unique_lst

print(unique_numbers([1, 2, 4, 5, 6, 7, 8, 8]))
