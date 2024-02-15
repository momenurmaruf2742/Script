import re

def password_strength_checker(password):
    if len(password) < 10:
        return "Password length should be at least 10 characters."
    if not re.search("[A-Z]", password):
        return "Password must contain at least one upper case letter."
    if not re.search("[a-z]", password):
        return "Password must contain at least one lower case letter."
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."
    if not re.search("[!@#$%^&*()-_+=]", password):
        return "Password must contain at least one special character."
    return "The password is correct."

password = input("Enter your password: ")
print(password_strength_checker(password))