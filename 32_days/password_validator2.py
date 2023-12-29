def password_validator():
    """ Request user to input password, and it should validate
        the password as follows: password should be 8 character
        long, have at least 1 uppercase char and number
    """
    def meet_requirement(st: str) -> bool:
        errors = [] 
        if len(st) < 8:
            errors.append("Please add at least one capital"
                    "letter to your password")
        elif not any(char.isdigit() for char in st):
            errors.append("Please add at least 1 digit to"
                    "your password")
        elif not any(char.islower() for char in st):
            errors.append("Please add at least 1 lowercase"
                    "letter to your password")
        elif not any(char.isupper() for char in st):
            errors.append("please add at least one uppercase"
                    "letter to your password")
        
        if len(errors) > 0:
            print("check the following errors")
            print(str(errors))
            del errors[:]
        else:
            return True


    while True:
        passwd = input("enter password to be validated: ")
        if meet_requirement(passwd):
            return f"Your password is {passwd}"
print(password_validator())
