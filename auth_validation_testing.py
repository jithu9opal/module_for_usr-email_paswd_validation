from auth_validation_module_by_G2 import validate_username, validate_email, validate_password

# get valid username or email
while True:
    user_input = input("Enter username or email: ")

    if validate_username(user_input) or validate_email(user_input):
        print("Username / Email format is valid")
        break
    else:
        print(" Invalid username/email format. Try again.\n")


# get valid password
while True:
    password = input("Enter password: ")

    if validate_password(password):
        print("Password format is valid ")
        break
    else:
        print(
            "Invalid password.\n"
            "Password must contain:\n"
            "- At least 8 characters\n"
            "- One uppercase letter\n"
            "- One lowercase letter\n"
            "- One digit\n"
            "- One special character (@$!%*?&)\n"
        )


print(" Validation successful! You can create an account now.")
