def read_backwards(st:str):
    """ Read a string backward"""
    back  = " ".join(reversed(st.split()))

    return back

str1 = "the love is real"
print(read_backwards(str1))
