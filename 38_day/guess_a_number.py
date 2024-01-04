from random import randint

def guess_a_number():
    """ check if user input is equal to the random generated
        number.
    """
    n = 3
    the_rand = randint(0, 9)

    while True:
        user_in = int(input('guess the number(1 - 9): '))

        if user_in == the_rand:
            print("you guess right!!")
            break
        else:
            if user_in > the_rand:
                print("your guess is too high")
            else:
                print("your guess is too low")
        n -= 1
        if n == 0:
            print("You loose")
            break

guess_a_number()
