def user_name():
    """generate username from provided email address"""
    email = input('enter your email: ').split('@')

    username = email[0]
    
    return f"your username is {username}"

print(user_name())
