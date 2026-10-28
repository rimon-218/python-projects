from datetime import datetime

def add_numbers(*numbers:int):
    return sum(numbers)

def show_time():
    return datetime.now().strftime("%H:%M:%S")

print("Sum :",add_numbers(10,20,30))
print("Time :",show_time())



"""

dry run:

add_numbers:
10,20,30

*numbers:
10,20,30 reseved

sum():
10+20+30=60

show_time():
'n datetime.now()
'n current time retirned



step    ।     function        ।      input      ।     output 
--------------------------------------------------------------------
1       ।     add_time        ।     10,20,30    ।       60  
2       ।     show_time       ।        -        ।   current time


"""