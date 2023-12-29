def average_calories():
    """ Calculate the average user calories intake from the
        user input for any number of specified days
    """
    calories = []
    while True:
        cal_num = input("Enter number of calories (type 'done' to finish): ")
        if cal_num.lower() == "done":
            break
        try:
            calories.append(int(cal_num))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(calories) > 0:
        return sum(calories) / len(calories)
    else:
        return 0  # Handle the case where the user didn't input any calories

# Example usage:
average = average_calories()
print(f"Average calories: {average}")

