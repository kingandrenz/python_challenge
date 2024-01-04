def translate(st: str):
    """ takes a string as param, add 'yay' at the end if the
        word starts with a vowel letter, if the word starts with
        any thing other than a vowel letter, we move the first 
        letter to the end and add 'ay' to the back.
    """
    def pig_latin(st:str):
        vowel= 'aeiou'

        if st[0] in vowel:
            st = st + 'yay'
        else:
            st = st[1:] + st[0] + 'ay'

        return st

    return ' '.join(pig_latin(word) for word in st.split())

a = 'i love python'

print(translate(a))
