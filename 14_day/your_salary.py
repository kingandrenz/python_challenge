def your_salary():
    """ takes input: teacher's name, number of periods taught
        in a month and rate per period. and calculate teacher's
        salary.
    """

    teacher_name = input("please enter teacher's name: ")
    num_periods = int(input("enter number of periods: "))
    rate = int(input("enter rate: "))

    if num_periods > 100:
        extra_time = (num_periods - 100) * 25
        normal_time = (num_periods - (num_periods - 100)) * rate
        
        salary = extra_time + normal_time
    else:
        salary = num_periods * 20

    result = f"Teacher:{teacher_name},\
            \nPeriods:{num_periods}\nGross salary: {salary:,}"
    return result

print(your_salary())


