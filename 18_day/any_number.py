def any_number(*args) -> float:
    """ Receives any number of arguments and return
        their sum.
    """
    if not args:
        return 0.0

    return sum(args) / len(args)

print(any_number(12, 90, 12, 32))
