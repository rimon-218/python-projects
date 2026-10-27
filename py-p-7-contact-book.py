import json

contact={
    "name":"Rahim",
    "phone":"01700000000"
}

try:
    with open("contact.json","w")as file:
        json.dump(contact,file)

    with open("contact.json","r")as file:
        data=json.load(file)

    print(data)

except Exception as e:
    print("Error:",e)



"""

dry run:

contact:

name=Rahim
phone=01700000000

open("contact.json","w")
'n File Created 

json.dump()
'n contact saved

open("contact","r")
'n File open

json.load()
'n Data read

data=contact

print(data)



trace table:


step    ।   Operation       ।   Data   
----------------------------------------------------------
1       ।   Create contact  ।    Rahim  
2       ।   Write Json      ।    contact.json
3       ।   Read Json       ।    Rahim
4       ।   Print           ।    Contact information

"""