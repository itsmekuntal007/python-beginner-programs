r=input("Is the restaurant open?(Y/N):")
if r=='Y':
    print("Restaurant is open")
    f=input("Is listed food available?(Y/N):")
    if f=='Y':
        print("Listed Food is available")
        p=input("Want to place order?(Y/N):")
        if p=='Y':
            print("Order placed! Thank you!")
        else:
            print("Order not placed")
    else:
        print("Sorry! Listed food not available")
else:
    print("Sorry!! Restaurant is closed")