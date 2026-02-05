actual=int(input("Enter the actual cost of anything: "))
selling=int(input("Enter the selling price of the item: "))

if selling>actual:
    profit= selling-actual
    print("Profit is: ", profit)

elif selling<actual:
    loss= actual-selling
    print("Loss is: ", loss)

else:
    print("No profit no loss")