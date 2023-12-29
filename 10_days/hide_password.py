def hide_password() -> str:
    """ takes an input from user and return a hidden password"""
    password = input('please enter your password: ')
    hidden_pass = ''
    for i in password:
        hidden_pass += '*'
    return f"Your password is {len(password)} character long {hidden_pass}"

print(hide_password())
