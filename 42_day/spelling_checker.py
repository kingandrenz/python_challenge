from textblob import TextBlob

def spelling_checker():
    """Ask the user for a word and suggest the correct word if the
        entered word is wrong.
    """
    while True:
        user_input = input('Enter a word: ')
        blob = TextBlob(user_input)

        corrected_blob = blob.correct()

        if user_input == corrected_blob:
            print(f"You entered: {user_input}")
            break
        else:
            print(f"Did you mean to type '{corrected_blob}'?")

            while True:
                ansa = input("Enter Yes/No: ")

                if ansa.lower() == 'no':
                    print("Please enter the word again.")
                    break
                elif ansa.lower() == 'yes':
                    return f"\nYou entered: {corrected_blob}"
                    break
                else:
                    print("Invalid response.")



print(spelling_checker())

