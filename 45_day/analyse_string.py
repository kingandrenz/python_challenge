import string

def analyse_string(st: str) -> dict:
    """ take a string as arg, and return the number of special
        characters, numeric char and total char excluding white
        space.
    """
    st = st.replace(" ", "")
    s_char = len([x for x in st if x in string.punctuation])
    n_char = len([x for x in st if x in string.digits])
    t_char = len(st)

    return {"special_char": s_char, "numeric_char": n_char, "total_char": t_char}


test_st = """ Python has a string format operator %. This functions
analogously to printf format strings in C, e.g. "spam=%s
eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2
"""

print(analyse_string(test_st))

