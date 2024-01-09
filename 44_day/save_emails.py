def save_emails():
    """ ask user to input email and store it in a csv file
    """


    while True:
        email = input("Enter email: ")
        
        if email.lower() == 'done':
            break
        else:
            with open('email.csv', 'a') as file:
                file.write(email+'\n')

    return "Emails saved succeffyly"


print(save_emails())



