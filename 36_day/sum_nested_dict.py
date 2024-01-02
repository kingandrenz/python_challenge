def sum_nested_dict(dic:dict) -> int:
    """ takes a dict and return the sum of values in the dict"""
    s_count = 0
    for k in dic.values():
        if type(k) == int:
            s_count += k
        else:
            if type(k) == dict:
                for l in k.values():
                    if type(l) == int:
                        s_count += l
                    else:
                        if type(l) == dict:
                            s_count += sum(l.values())
    return s_count

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e':3, 'f': 4}}, 'g': 5}
print(sum_nested_dict(nested_dict))
