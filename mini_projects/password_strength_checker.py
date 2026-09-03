password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) < 8:
    print("Password Strength: Weak")
elif has_upper and has_lower and has_digit and has_special:
    print("Password Strength: Strong")
elif has_upper and has_lower and has_digit:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")