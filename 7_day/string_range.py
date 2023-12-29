def string_range(n):
    """takes a single number and return a string of it range"""
    str_range= ""

    for i in range(n):
        a = '.'
        str_range += str(i)+a

    return str_range


#Or we can do:
"""
def string_range(n:int):
    x = [str(i) for i in rang(n)]

    x = ".".join(x)

    return x
"""

print(string_range(6))

