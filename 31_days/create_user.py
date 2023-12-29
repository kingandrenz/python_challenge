def create_user():
    """ ask user for detail and store it in a dictionary
        and return 'User saved succesfully', the ask user
        to login by inputing their details.
    """
    database = {"name": input("please enter name: "), 
                "age" : int(input("enter your age: ")),
                "password": input("enter password: ")
                }
    print("User saved. Please login")
    print()

    while True:
        name = input("please enter username: ")
        passwd = input("Enter password: ")

        if name == database["name"] or passwd == database["password"]:
            return "\nLogged in successfuly"
        else:
            print("\nWrong password or username, please try again")


   
print(create_user())
