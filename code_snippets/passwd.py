# Password Strength Checker
password = input("Enter a new password : ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for char in password:
    if char.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")