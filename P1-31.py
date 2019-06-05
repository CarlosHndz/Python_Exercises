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
   
    # NOTE: In order to represent currency properly you
    # need to use cents as an integer and divide by 100 to convert to dollars.
    # Using floating point is not accurate to properly represent currency.

    # Currency represented in cents. Divide by 100 to convert to dollars
    currency = (10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1)
    total_change = 0
    change = {}
    difference = int(payment * 100) - int(charge * 100) #convert to cents
    
    # while the change is > 0, divide the amount by the highest possible bill 
    # and coin denominations
    while difference >= 1:
        for value in currency:
            if difference >= value:
                change[value] = int(difference // value)
                difference %=  value
                
    # print the charge amount along with the payment and the breakdown of the 
    # calculated change with the minimum amount of bills/coins possible.        
    print("")
    print("Charge amount: $", charge)
    print("Payment amount: $", payment)
    print("")
    print("Your change consists of: ")
    
    for key, value in change.items():
        total_change += (key * value)
        print(value, " x $", (key/100), " = $", ((key * value)/100))

    print("For a total change of: $", (total_change/100))       
                

# test the function    
make_change(4.01, 10.00) # $5.99
make_change(3.45, 20.00) # $16.55
make_change(16.87, 50.00) # $33.13
make_change(0.99, 1.00) # $0.01
