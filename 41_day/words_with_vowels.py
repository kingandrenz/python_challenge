def words_with_vowels(st: str) -> list:
    """ Takes a string of words and return a list of only
        those with vowels in them.
    """
    vowels = 'aeiou'
    st = st.lower()
    v_list = [word for word in st.split() if any(char in vowels for char in word)]

    return v_list

print(words_with_vowels("You have no rhythm,"))
