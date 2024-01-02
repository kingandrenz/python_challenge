def count(st:str) -> dict:
    """ take a string as argument and return a dict"""
    return {i: st.count(i) for i in st}

print(count("hello"))
