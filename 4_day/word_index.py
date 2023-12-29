def word_index(my_list:list):
    """ return the index of the longest word in a list 
        and zero (0) if they are equal
    """
    if not max(my_list, key=len):
        return 0
    else:
        return my_list.index(max(my_list, key=len))

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))
print(word_index(words2))
