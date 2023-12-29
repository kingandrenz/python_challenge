import math

def divide_or_square(n):
    """ Takes one argument and renturns its square root if it is divisible
    by 5 or it's remainder if not dovisible by 5"""

    if n % 5 == 0:
        _sqrt = math.sqrt(n)
        print(f"{n} is divisible by 5 and the ansa is: {_sqrt:.2f}")
    else:
        remainder = n % 5

        print(f"{n} is not divisible by 5, it's remainder is: {remainder}")


my_input = int(input("please enter a number: "))

divide_or_square(my_input)



