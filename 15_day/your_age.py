def your_age():
    """ ask student for name, and check database if the student 
        existthen return name and age of the user
    """
    stu_name = input("enter your name: ").lower()

    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

    if stu_name in names_age:
        return f"Hi, {stu_name}, your are {names_age[stu_name]} years old."
    else:
        print("OOPs!!, your name is not in the database")
        usr_name = input("please enter your name: ").lower()
        age = int(input("please enter your age: "))

        names_age[usr_name] = age
        return f"Hi, {usr_name}, you added {age} years old."

print( your_age())
