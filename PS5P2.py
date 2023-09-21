#inputphase
item = input("Enter Item")
Qty = float(input("Enter Quantity ordered"))

#processphase
if item=="A":
  unitprice = 10.00
else:
  unitprice = 20.00

extprice = (Qty * unitprice)

print("Item Ordered:",item)
print("Unit Price: $", unitprice)
print("Extended Price:$",extprice)
     