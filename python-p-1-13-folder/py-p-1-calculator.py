def calculator(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        return "invalid value"


a=10
b=5
op="+"

result=calculator(a,b,op)

print(result)

"""
dry run:

a=10
b=5
op=+
calculator(10,5,+)
op=="+"
10+5
result=15
print(15)
output:15


trace table:

step    ।   a   ।   b   ।   operator  ।   result
--------------------------------------------------
1       ।   10  ।   5   ।       +     ।     -
2       ।   10  ।   5   ।       +     ।     15

"""