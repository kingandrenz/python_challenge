students = ['Male', 'Female', 'female', 'male', 'male', 'male',
 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']


count_male = 0
count_female = 0

for x in students:
    if x.lower() == 'male':
        count_male += 1
    else:
        x.lower() == 'female'
        count_female += 1
        
tuple_list = [('Male',count_male), ('Female',count_female)]
print(tuple_list)
