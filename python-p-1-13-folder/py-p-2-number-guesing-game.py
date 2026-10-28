import random 

secret=random.randint(1,10)

for i in range(3):
    guess=int(input("Guess :"))
    if guess==secret:
        print("Corect!")
        break
    elif guess<secret:
        print("To low")
        continue
    else:
        print("To high")
else:
    print("Game over")


"""

dry run:

dori secret=7

i=0
guess=5
5==7'false
5<7'true
output=To low

i=1
guess=9
9==7'false
9<7'false
continue
output=To high

i=2
guess=7
7==7'true
output=Correct!
break



trace table:

step    ।   i   ।   secret   ।   guess  ।     result
--------------------------------------------------------
1       ।   0   ।      7     ।     5    ।     To low
2       ।   1   ।      7     ।     9    ।     To high
3       ।   2   ।      7     ।     7    ।     Coreect!
 

"""