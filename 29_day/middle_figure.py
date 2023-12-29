def middle_figure(a: str, b: str) -> str:
    """ Takes two string as argument and join them,
        then finds the middele element and return it
        if there no middle element it should return 
        "not middle figure".
    """
    j_str = (a + b).replace(" ", "")
    
    if len(j_str) % 2 != 0:
        return j_str[int((len(j_str) + 1) / 2) - 1]
    else:
        return f"no middle figure"

print(middle_figure("make love", "not wars"))
