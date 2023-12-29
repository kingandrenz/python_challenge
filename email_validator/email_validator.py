def email_validator(ls: list) -> list:
    """ Take a list of email and return the valid ones
    """
    valid_e = []

    for i in ls:
        if i[0] != '@' and any(j == '@' for j in i) and i[-4:] == '.com' and '@'.count(i) == 1:
            valide_e.append(i)

    if len(valid_e) < 1:
        return ls
    else:
        return valid_e

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']

print(email_validator(emails))
