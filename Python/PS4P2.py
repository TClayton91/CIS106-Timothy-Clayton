#input phase
priceper = float(input("Enter purchase price of each share"))
currentprice = float(input("Enter current price of share"))
quantity = float(input("Enter Quantity of shares"))

#process phase
valueofstock = (currentprice - priceper) * quantity

#outputphase
print("Value of stock =",valueofstock)