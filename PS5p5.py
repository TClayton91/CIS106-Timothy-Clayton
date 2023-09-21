#input phase
lastname = input("Enter Last Name")
grosspay = input("Enter gross Income")
nodep = input("Enter Dependents")

#process phase
adjustgross = float (grosspay) - 12000.00 * float(nodep)

if adjustgross > 50000:
  tax = adjustgross * 0.20
else:
  tax = adjustgross * 0.10

if tax < 0:
  tax = 100.00



print(lastname)
print("Gross Income:  $", grosspay)
print("Number of Dependents: ",nodep)
print("Adjusted Gross:  $", adjustgross)
print("Income Tax:   $", tax)