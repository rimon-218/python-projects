import requests

try:
    response=requests.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )

    data=response.json()
    print("Title",data["title"])
except Exception as e:
    print("Error:",e)


"""

dry run:


requests.get()
'n api requests sent

api response resived

response.json()
'n json converted to python dictionary

data["title]
'n title pauagelo

print()
'n title displyed



trace table:

step    ।       opertion        ।    result   
-------------------------------------------------------
1       ।   api request         ।    response    
2       ।   json cenvertion     ।    dictionary 
3       ।   dictionary accses   ।    title 
4       ।   print               ।    title shown     


"""