import string

def check_pangram(st:str) -> bool:
    """ Takes a string and check if it is pangram and return
        a boolean
    """
    st = st.lower()
    st_set = set(char for char in st if char.isalpha())
    strings_ = set(string.ascii_lowercase)
    pangram = st_set == strings_

    return pangram

print(check_pangram('the quick brown fox jumps over a lazy dog'))
