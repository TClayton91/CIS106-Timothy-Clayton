#input phase
qty = float(input("Enter Quantity Here"))

#process phase
if qty>=1000:
  unitprice = 3.00
else:
  unitprice = 5.00

extprice = qty * unitprice
tax = extprice * 0.07
total = tax + extprice

print(" Quantity orders",qty)
print(" Unit Price $", unitprice)
print("Extended Price $0", extprice)
print("Tax $", tax)
print("Total $", total)