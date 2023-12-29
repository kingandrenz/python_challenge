def string_length(st:str) -> dict:
    """ 
        arg: string (words and spaces)
        return: dictionary (word:len(word), ..)

    """
    return {word: len(word) for word in st.split()}

print(string_length('Hi my name is Richard'))
