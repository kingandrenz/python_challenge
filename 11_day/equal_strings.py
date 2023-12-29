def equal_strings(str1, str2):
    """Compare two string and return true or
        false if they have same character and length
    """
    return len(str1) == len(str2) and set(str1) == set(str2)

print(equal_strings('love', 'evol'))
