def add_hash(st:str):
    """takes a string and add a '#' betweed the words"""
    return '#'.join(st)

def add_underscore(st:str):
    """ removes the '#' in a string and replace it with a '-'"""
    new_str = st.replace('#', '-')

    return new_str

def remove_underscore(st:str):
    """ remove the remove the underscore in a string and 
        replace it with ''
    """
    new_str = st.replace("-", "")

    return new_str

print(remove_underscore(add_underscore(add_hash('Python'))))
