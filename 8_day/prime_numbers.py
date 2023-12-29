def prime_numbers():
    """ take users input and return all prime numbers
        within the range
    """
    usr_input = int(input("enter a number: "))

    prime_num = [num for num in range(2, usr_input + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

    return prime_num
print(prime_numbers())
