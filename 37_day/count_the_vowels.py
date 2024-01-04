def count_the_vowels(st:str) -> int:
    """ takes a string as arg and return the number of set
        vowels that appears
    """
    st = set(st)
    vowel = set('AEIOUaeiou')
    count = 0
    
    for i in st:
        if i in vowel:
            count += 1
    return f"there are {count} set of vowels in the string"


print(count_the_vowels("Hello"))

