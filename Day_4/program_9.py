def password(pas):
    passwords=pas.split(",")
    valid_passwords = []
    for password in passwords:
        if 6 <= len(password) <= 12:
            has_lower = any(c.islower() for c in password)
            has_upper = any(c.isupper() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in "$#@ " for c in password)
            if has_lower and has_upper and has_digit and has_special:
                valid_passwords.append(password)
    print(",".join(valid_passwords))
pas = input("Enter passwords separated by commas: ")
password(pas)