import winsound
from datetime import datetime
import time

def alarm():
    """ creates an alarm clock by asking the user for input and
        triggering the alarm to go off at the inputted time.
        returns the time the alarms will go off.
    """
    a_time = input("Please enter alarm time (HH:MM): ")
    time_now = datetime.now().strftime("%H:%M")
    a_time2 = datetime.strptime(a_time, "%H:%M")

    try:
        hrs, mins = map(int, a_time.split(':'))

        if 0 <= hrs < 24 and 0 <= mins < 60:
            if a_time2 >= datetime.strptime(time_now, "%H:%M"):
                print(f"The alarm is set for {hrs}:{mins}.")

                time_in_sec = hrs * 3600 + mins * 60

                time.sleep(time_in_sec)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            else:
                 print("Your inputted time is behind the current time.")

        else:
            print("Invalid input, please enter a valid time.")

    except ValueError:
        print("Invalid input. Please enter the time in this 'HH:MM' format.")

# Call the alarm function
alarm()

