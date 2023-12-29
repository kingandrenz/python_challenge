def password_validator():
    """ Request user to input password, and it should validate
        the password as follows: password should be 8 character
        long, have at least 1 uppercase char and number
    """
    def meet_requirement(st: str) -> bool:
        try:
            if len(st) < 8 and any(char.isupper() for char in st):
                raise ValueError("password must be equal to or greater than 8")
            if not any(char.islower() for char in st):
                raise ValueError("password must contain @ least 1 lowecase letter")
            if not any(char.isdigit() for char in st):
                raise ValueError("password must contain at least a digit")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


    while True:
        passwd = input("enter password to be validated: ")
        if meet_requirement(passwd):
            return passwd
print(password_validator())
