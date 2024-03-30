import re
name = input("Enter the name: ").strip()
phone = input("Enter the phone number: ").strip()
if re.search("^[0-9]{11}$",phone):
    print(name)
    print(phone)
else:
    print("invalid phone number")