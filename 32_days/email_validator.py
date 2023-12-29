def email_validator(emails: list) -> list:
    """ check if email is valid and return list of valid emails
        return original list of email of there non valid email
    """
    valid_e = []

    for email in emails:
        if email.count('@') == 1 and not email.startswith('@'):
            if email.endswith('.com'):
                valid_e.append(email)

    if valid_e:
        return valid_e
    else:
        return "All emails are invalid"

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']

print(email_validator(emails))
