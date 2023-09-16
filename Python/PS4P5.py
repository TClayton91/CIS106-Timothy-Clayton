#input phase
fixedcosts = float(input("Enter Fixed Costs"))
priceperunit = float(input("Enter Price Per Unit"))
costperunit = float(input( "Enter Cost Per Unit"))

#process phase
breakevenpoint = fixedcosts / (priceperunit-costperunit)

#outputphase
print("Breakeven Point: $ :",breakevenpoint)


