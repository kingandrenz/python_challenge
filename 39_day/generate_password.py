import random
import string

def generate_password():
    """Generate password for user (weak, strong, very strong)
        according to user preference.
    """
    print("Password Generator")
    print()
    print("How strong do you want your password to be?")
    user_input = int(input("\npress 1,2, 3, for weak, strong and very strong respectively: "))
    pass_len = 0

    characters = string.ascii_letters + string.digits + string.punctuation
    if user_input == 1:
        pass_len = 5
    elif user_input == 2:
        pass_len = 8
    elif user_input == 3:
        pass_len = 12

    password = ''.join(random.choice(characters) for _ in range(pass_len))

    return password

print(generate_password())

