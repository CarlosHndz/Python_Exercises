'''
Write a program that can "make change". Your program should take two numbers
as input, one that is a monetary amount charged and the other that is a 
monetary amount given. It should then return the number of each kind of bill
and coin to give back as change for the difference between the amount given
and the amount charged. The values assigned to the bills and coins can be
based on the monetary system of any current or former government. Try to 
design your program so that it returns as few bills and coins as possible.
'''


def make_change(charge, payment):
    # Bill denominations: $100, $50, $20, $10, $5, $1
    # coin demonimations: $0.25, $0.10, $0.05, $0.01
    bills_coins = (100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01)
    change = {}
    difference = float(payment) - float(charge)
    
    # while the change is > 0, divide the amount by the possible bills and coins
    while difference >= 0.1:
        for m in bills_coins:
            print("m value = ", float(m))
            print("Difference value = ", difference)
            if difference >= float(m):
                divisor = difference // m
                difference %=  m
                change[m] = divisor
            
                print(change)
                
                
    
make_change(4.01, 10.00)
