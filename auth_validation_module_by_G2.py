# auth_validator.py

import re

# validate username
def validate_username(username):
    pattern = r'^[a-zA-Z0-9_]{4,15}$'
    return bool(re.match(pattern, username))


# validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# validate password
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, password))


# validate login input (username OR email + password)
def validate_login(user_input, password):
    if validate_username(user_input) or validate_email(user_input):
        return validate_password(password)
    return False
