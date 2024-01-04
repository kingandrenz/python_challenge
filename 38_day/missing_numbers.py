def missing_numbers(ls:list) -> list:
    """ take a list of sequence and find the missing numbers 
        in the sequence.
    """
    seq_list = [i for i in range(1, ls[-1]+1)]

    missing_num = [x for x in seq_list if x not in ls]

    return missing_num

list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

print(missing_numbers(list1))
