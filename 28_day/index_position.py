def index_position(st:str) -> list:
    """ Takes a string as argument and return a list of the
        positional index of the lowercase letters.
    """
    index_p = [st.index(x) for x in st if x.islower()]

    return index_p

print(index_position("LovE"))
