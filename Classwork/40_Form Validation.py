import re

def validate_name(name):
    pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
    return bool(re.fullmatch(pattern, name))
name = input()
print(validate_name(name))



def validate_email(email):
    pattern = r'^[a-z0-9._]+@[a-z.-]+\.[a-z]{2,}$'
    return bool(re.fullmatch(pattern, email))

email = input()
print(validate_email(email))


