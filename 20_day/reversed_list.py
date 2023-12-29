def reversed_list(st: str) -> list:
    """ return a list of the word that has at least one upper case in them,
    in the reverse order of their appearance uppercasse in it
    """
    lst = [word[:: -1] for word in st.split() if any(letter.isupper() for letter in word)]


    return lst

str1 = 'leArning is hard, bUt if You appLy youRself ' \
 'you can achieVe success'

print(reversed_list(str1))
