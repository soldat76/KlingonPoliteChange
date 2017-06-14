## KlingonPoliteChange.py
##
##
## This program will compute the "polite change" a Klingon shop owner will give to his/her Klingon customers
##
##
## The lru is currently worth 90 monetary units (mu)
## The talon is currently worth 30 mu
## The darsek is currently worth 10 mu
## The shhhrok is currently worth 1 mu
##
##
## Aster Fan
##
## June 2017

# These variables are defined beforehand in case the values of Klingon money change with respect to monetary units.
lru = 90
talon = 30
darsek = 10
shhhrok = 1

# This statement is printed out to the user to let them know what this program does.
print("\nThis program will calculate the amount of polite change in Klingon money from monetary units (mu)!\n")

# The variable purchaseAmount is the value of the purchase in mu.
while True:
    # Ask the user for a non-negative integer of the total amount of monetary units of their purchase.
    purchaseAmount = input("\nEnter the amount of mu of the purchase total (non-negative integer)!\n> ")
    
    # Make sure purchaseAmount is not an alphabetical character
    if purchaseAmount.isalpha():
        print("\nAlpha characters are not allowed. Please try again.")
        
    # Make sure that the purchaseAmount variable is a positive integer.
    else:
        purchaseAmount = int(purchaseAmount)
        if purchaseAmount <0:
            print("\nYou can't have a negative value here. Please try again.")

    # This rejects the value of 0 for the variable purchaseAmount.
        elif purchaseAmount == 0:
            print("\nHaving a purchase total of 0 would defeat the purpose of this calculator. Please try again.")

    # Stop the while loop when conditions are met.
        else:
            break

# The variable payingAmount is the amount of mu the customer is paying with.
while True:
    # Ask the user for the total amount of monetary units that the customer is paying with.
    payingAmount = input("\nEnter the amount of mu the customer is purchasing with (non-negative integer)!\n> ")
    
    # Make sure payingAmount is not an alpha character.
    if payingAmount.isalpha():
        print("\nAlpha characters are not allowed. Please try again.")
        
    else:
        payingAmount = int(payingAmount)
        
        # If the customer has less than the amount needed to complete a purchase, the program ends.
        if payingAmount < purchaseAmount:
            print("\nThis customer doesn't have enough mu for this purchase!")
            break
        # If the customer has paid the purchase with exact change, the program ends.
        elif payingAmount == purchaseAmount:
            print("\nThis customer has paid with exact change!")
            break
        
        # These line(s) will compute the amount of "polite" change needed using lru, talon, darsek, and shhhrok.
        elif payingAmount > purchaseAmount:
            changeDisplay = payingAmount - purchaseAmount   # changeDisplay is a variable that is printed at the end to show user the total change in mu.
            change = payingAmount - purchaseAmount  # The variable change is the change after the purchase.
        
            changeLru = change//lru     # changeLru is a variable that tells us the correct amount of lru to dispense.
            change%=lru     # This will calculate the remaining amount of change left after calculating lru.

            changeTalon = change//talon     # changeTalon is the amount of talon to dispense to customer.
            change%=talon   # This line calculates the amount of change left after calculating talon.

            changeDarsek = change//darsek   # changeDarsek is the amount of darsek to dispense to customer.
            change%=darsek  # This line calculates the amount of change left after calculating darsek.

            changeShhhrok = change//shhhrok     # changeShhhrok is the amount of shhhrok to dispense to customer.
            change%=shhhrok     # This line calculates the amount of change left after calculating shhhrok (should be zero at this point).

        # This statement will be shown to the shop owner so he/she will know how to dispense change in a polite manner.
        # The line below prints the result of the calculation.
            print("\nThe polite way to give back Klingon change of **%i mu** is: \n\t%i lru (%i mu), \n\t%i talon (%i mu), \n\t%i darsek (%i mu), \n\t%i shhhrok (%i mu)."
              %(changeDisplay,changeLru,lru,changeTalon,talon,changeDarsek,darsek,changeShhhrok,shhhrok))
            
            input("\nThank you for using this calculator. To exit, press enter.")
            break
            
                
