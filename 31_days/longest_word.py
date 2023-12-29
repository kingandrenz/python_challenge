def  longest_word(ls:list):
    """ take a list of word as argument and return longest
        and the number of letters in that word.
    """
    l_list = [max(ls, key=len), len(max(ls, key=len))]

    return l_list
print( longest_word(['Java', 'JavaScript', 'Python']))
