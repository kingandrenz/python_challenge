def lower_case(my_list):
    """ return a tuple of names in small letters"""
    names = []

    for i in my_list:
        if i.islower():
            names.append(i)

    sorted_names = sorted(names, reverse=True)
    print(tuple(sorted_names))

l_names = ["kerry", "dickson", "John", "Mary",
 "carol", "Rose", "adam"]

#or we can use the below method

lower_case(l_names)

"""
names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]

my_list = []

for i in sorted(names, reverse=True):
    if i.islower():
    my_list.append(i)
    tuple_name = tuple(my_list)

print('The number of student in school is' tuple_name')
"""
