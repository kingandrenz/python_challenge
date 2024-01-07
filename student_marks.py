import string

def student_marks():
    """ Take user input (name and mark) respectively and store it in a dictionary.
        Returns the dictionary.
    """

    print("Enter student details, enter 'done' when done\n")
    stu_database = {}

    while True:
        user_name = input("Enter student name: ")

        if user_name.lower() == 'done':
            break

        try:
            if any(char in string.punctuation or char.isdigit() for char in user_name):
                raise NameError("Please enter a valid name without digits or punctuation.")

            user_mark = int(input("Enter student mark: "))

            if not (0 <= user_mark <= 100):
                raise ValueError("Please enter a valid score between 0 and 100.")

            stu_database[user_name] = stu_database.get(user_name, 0) + user_mark

        except (NameError, ValueError) as e:
            print(f'Error: {e}')

    return stu_database

print(student_marks())

