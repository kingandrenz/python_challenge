import emoji

def python_snakes(row: int):
    """take a number as arg and return a pyramid of snake
        using the number
    """
    h = row
    for i in range(row):
        #print spaces
        for j in range(h):
            print(" ", end='')

        h -= 1

        for k in range(0, i + 1):
            print(emoji.emojize(":snake:"), end='')
        print()


pyra = int(input("enter number: "))
python_snakes(pyra)

