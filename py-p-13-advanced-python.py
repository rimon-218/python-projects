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
