def repeated_name(ls:list) -> str:
    """ take a list of name as argument and return the most 
        repeated name
    """
    return f" the most repeated name is {max(ls)}"

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(name))
