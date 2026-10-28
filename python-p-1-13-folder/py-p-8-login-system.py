import json
import re

username="rahim123"
password="python123"

if re.match(r"^[a-zA-Z0-9]+$",username):
    print("Username valid")
else:
    print("Invalid username")

users={
    username:password
}

with open("users.json","w")as file:
    json.dump(users,file)

print("Account created")


"""

dry run:

username=rahim123

regex checks:
rahim123 'n valid

password=python123

users={
    username:password
}

Json file:
users.json

account created


trace table:

step    ।     username        ।      regex      ।     result 
-----------------------------------------------------------------------
1       ।     rahim123        ।      valid      ।   username valid  
2       ।     rahim123        ।      valid      ।   saved to json




"""