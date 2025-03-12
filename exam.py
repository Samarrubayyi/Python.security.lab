def is_valid_password(password):
    special_chars = {'^', '{', '}','(',')','[',']','_','-','+','*','/','\\','<','>'}

    if not (5 <= len(password) <= 10):
        return "Invalid Password"
    if any(c.isspace() for c in password):
        return "Invalid Password"
    if not any(c.isupper() for c in password):
        return "Invalid Password"
    if not any(c.islower() for c in password):
        return "Invalid Password"
    if not any(c.isdigit() for c in password):
        return "Invalid Password"
    if not any(c in special_chars for c in password):
        return "Invalid Password"

    return "Valid Password"


password = input("Enter a password: ")
print(is_valid_password(password))