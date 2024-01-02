def sum_nested_dict(dic:dict) -> int:
    """ takes a dict and return the sum of values in the dict"""
    t_sum = 0
    for value in dic.values():
        if isinstance(value, int):
            t_sum += value
        elif isinstance(value, dict):
            t_sum += sum_nested_dict(value)
    return t_sum

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e':3, 'f': 4}}, 'g': 5}
print(sum_nested_dict(nested_dict))
