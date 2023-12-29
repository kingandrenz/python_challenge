def count_words(st: str):
    """ takes a string and return return number of words
        in the string.
    """
    num_st = st.split()
    return f"{len(num_st)} words"


def count_elements(st: str) -> int:
    """ return num of element in a string excluding whitespace
    """
    count = 0
    for i in st:
        if i.isalpha():
            count += 1
    return f"{count} elements"

print(count_words("I love learning,"))
print(count_elements("I love learning,"))
