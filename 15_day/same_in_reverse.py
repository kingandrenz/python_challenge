def same_in_reverse(st: str):
    """ rverse an inputed user string and check if is the 
        same as the original string and return True or false,
        respectively.
    """

    if st == st[::-1]:
        return True
    else:
        return False

print(same_in_reverse(input('enter a word: ')))
