def open_emails(n):
    """ Opens the opens and read the content of the csv file.
    """

    with open(n, 'r') as file:
        print(file.read())

open_emails('email.csv')
