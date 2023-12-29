def convert_numbers(lst: list) -> list:
    """Return a list of strings with comma separators."""
    str_lst = []
    for i in lst:
        # Convert the string to an integer before formatting
        num = int(i)
        str_lst.append("{:,}".format(num))

    return str_lst

lst = ['1000000', '2356989', '2354672', '9878098']
print(convert_numbers(lst))

