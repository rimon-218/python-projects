def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cannot divide by zero"

result=divide(10,2)

assert result==5
print("test passed")



"""
dry run:


divide(10,2)

a=10
b=2

10/2
'n 5

result=5

assert result==5
'n true

output:
 test passed



 trace table:

step    ।   a   ।    b   ।   result  ।   test    
-------------------------------------------------
1       ।   10  ।    2   ।     5     ।   true              




"""