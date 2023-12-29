def only_floats(a, b):
    """Returns 2 if a and b are float, and 1 if a or b is float"""
    if (type(a) == type(b) == float):
        return 2
    elif (type(a) == float or type(b) == float):
        return 1
    else:
        return 0

print(only_floats(2, 23))
print(only_floats(12.1, 23))
print(only_floats(13.1, 12.2))
