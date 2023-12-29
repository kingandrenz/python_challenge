from random import randint
def user_name() -> str:
    """Generates username from userinput by reversing the input
        and attaching a random issued numner from 0 - 9
    """
    name = input('please enter your name: ')
    username = name[::-1] + str(randint(0, 9))

    return username
print(user_name())

