from datetime import datetime, timedelta

def age_in_minutes() -> int:
    """calculate user years by subtracting user D.O.B
        from current year
    """
    yr = input('Enter year of birth: ')
    curr_date = datetime.now().date().year
    while not yr.isdigit() or len(yr) != 4:
        print('Please enter a four (4) digit number.')
        yr = input('Enter year of birth: ')

    yr = int(yr)

    if yr < 1900 or yr > curr_date:
        print('Your input is invalid')
        yr = (input('enter year of birth: '))

    #minutes_per_yr = 365.25 * 24 * 60
    age = curr_date - yr

    return timedelta(days=age * 365.25).total_seconds() / 60

#or  return minutes_pr_yr
print( age_in_minutes())
