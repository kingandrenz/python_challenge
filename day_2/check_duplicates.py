def check_duplicates(my_list):
    """check for duplicate in a list and return it"""
    duplicates = []
    for i in my_list:
        if my_list.count(i) > 1:
            duplicates.append(i)
    if duplicates:
        print(set(duplicates))
    else:
        print('No duplicate!')


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
check_duplicates(fruits)
check_duplicates(names)
