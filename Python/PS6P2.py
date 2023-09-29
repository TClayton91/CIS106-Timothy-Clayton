#inputphase
partnum = int(input("Enter Part Number"))
qty = input("Enter Quantity")
#processphase

if partnum == 10 or partnum== 55:
  unitprice = 1.00
elif partnum == 90:
  unitprice = 2.00
elif partnum == 70 or partnum == 80:
  unitprice = 3.00
else:
  unitprice== 5.00

total = float(qty) * unitprice

#printphase

print("Part Number:", partnum)
print("Unit Price:", unitprice)
print("Total: ", total)
