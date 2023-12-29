def sort_words(st:str) -> list:
    """ 
        arg: string
        return: list sorted in alphabetical order without
                duplicates.
    """

    st = st.replace(" ", "")
    new = sorted([i for i in set(st)])
    s_word = [",".join(new)]

    return s_word

print(sort_words("love life"))
