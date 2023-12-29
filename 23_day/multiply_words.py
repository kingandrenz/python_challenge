def multiply_words(st:str) -> int:
    """ multiply the lenght of each word in a string by the
        lenght of other words in the string, ingnore word if
        thre is capital letter in it
    """
    result = 1

    for word in st.split():
        if any(char.isupper() for char in word):
            continue
        else:
            result *= len(word)

    return result

s = "love live and laugh"
print(multiply_words(s))

