balance=1000

def add_money(*amounts):
    return sum(amounts)

def withdraw(balance,amounts):
    if amounts<=balance:
        return balance - amounts
    return balance

balance=withdraw(balance,500)


add=lambda x,y:x+y
balance=add(balance,add_money(200,300))
print(balance)



"""

dry run:

balance=1000

add_money(200,300)
'n 200+300
'n 500

add(1000,500)
'n 1500


withdraw(1500,500)
'n 1500-500
'n 1000

final balance=1000



step    ।   operation   ।   amounts   ।   balance  
-----------------------------------------------------
1       ।   starting    ।      -      ।     1000
2       ।   deposit     ।     500     ।     1500
3       ।   withdraw    ।     500     ।     1000



"""