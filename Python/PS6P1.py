#inputphase
qty = float(input("Enter Number of Quantity Here"))

#processphase

if qty > 10000:
  price = 10.00

elif qty > 5000:
  price = 20.00
else:
  price = 30.00


extprice = qty * price
tax = extprice * 0.07
total = tax + extprice

#printphase

print("Extended Price is $", extprice)
print("Tax is $", tax)
print("Total Is $", total)
