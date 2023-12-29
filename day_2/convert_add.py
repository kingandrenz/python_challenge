def convert_add(my_list):
    """ take a list of string as an argument and covert them to integers """

    new_list =[]
    
    for k in my_list:
        new_list.append(int(k))

    print(sum(new_list))


first_l = ["1", "3", "5"]
convert_add(first_l)
