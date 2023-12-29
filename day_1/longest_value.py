def longest_value(dick):
    """ returns the first longest value of the dictionary"""

    max_value = max(dick.values(), key=len)

    print(max_value)

fruits = {'fruit': 'apple', 'color': 'green'}
longest_value(fruits)
