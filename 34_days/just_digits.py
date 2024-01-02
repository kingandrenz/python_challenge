def just_digits(file_path: str):
    """ returning the digits in a csv file"""
    digit_elem = []

    with open(file_path, 'r') as file:
        reader = file.read().split()

        for row in reader:
            if row.isdigit():
                digit_elem.append(row)

    return digit_elem

csv_path = 'python.csv'

try:
    result = just_digits(csv_path)
    print(result)
except FileNotFoundError:
    print(f"File '{csv_path}' not found.")

