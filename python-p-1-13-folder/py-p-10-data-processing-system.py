numbers=[1,2,3,4,5]

square=[x*x for x in numbers]

even_numbers={
    x:x*x
    for x in numbers
    if x%2==0
}

def generate_numbers():
    for x in numbers:
        yield x

for value in generate_numbers():
    print(value)

"""

dry run:

numbers=[1,2,3,4,5]

list comprehension:

1 'n 1
2 'n 4
3 'n 9
4 'n 16
5 'n 25

squares:
[1,4,9,16,25]

dictionary comprehension:

2 'n 4
4 'n 16

even_numbers:
{2:4,4:16}

generator:

yield 1 
yield 2 
yield 3 
yield 4 
yield 5 



trace table:

step    ।   x    ।    x*x   ।     even? 
-----------------------------------------
1       ।   1    ।    1     ।     no 
2       ।   2    ।    4     ।     yes
3       ।   3    ।    9     ।     no
4       ।   4    ।    16    ।     yes
5       ।   5    ।    25    ।     no



"""