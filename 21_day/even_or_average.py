def even_or_average():
    """ Takes user input of five(5) numbers and return the
        largest even number in the users input. If there is
        no even number, it should return average of all 
        five user input
    """
    user = []
    count = 0

    while True:
        user.append(int(input('enter a number a number: ')))

        count += 1
        if count == 5:
            break

    even = [i for i in user if i % 2 == 0]

    if not even:
        return sum(user) / 5
    else:
        return max(even)

print(even_or_average())
