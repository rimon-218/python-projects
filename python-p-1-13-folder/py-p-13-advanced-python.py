def logger(func):

    def wrapper(*args,**kwargs):
        print("function started")
        result=func(*args,**kwargs)
        print("function finished")
        return result
    return wrapper


@logger
def add(a,b):
    return a+b

print(add(10,20))


"""

dry run:


@logger
'n add function-er opor decorator kaj korbe

add(10, 20)

wrapper(10, 20)

print:
Function started

func(10, 20)
'n 10+20
'n 30

print:
Function finished

return 30

Final output:
30



trace table:


step    ।     Function     ।   a   ।  b   ।  Result   
-------------------------------------------------------
1       ।   add            ।   10  ।  20  ।     -    
2       ।   wrapper        ।   10  ।  20  ।     -
3       ।   add            ।   10  ।  20  ।     30     


"""
