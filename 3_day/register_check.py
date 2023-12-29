def register_check(dick):
    """checks how many student are in school and return the number"""
    present = list(dick.values()).count('yes')
    print(f"there are {present} student in school today")

register = {'Michael':'yes','John': 'no', 
 'Peter':'yes', 'Mary': 'yes'}
register_check(register)
