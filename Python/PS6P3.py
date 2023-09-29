#inputphase
principle = float(input("Enter Principle amount"))
yearstomature = float(input("Enter Years to Maturity"))
#processphase

if principle >= 100000 and yearstomature == 5:
  interestrate = 0.06
elif principle >= 500000 and principle <100000 and yearstomature == 10: 
  interestrate = 0.05
elif principle >= 50000 and principle < 100000 and yearstomature == 5:
  interestrate = 0.04
else:
  interestrate = 0.02

firstyearinterest = float(principle) * interestrate

#printphase

print("Principle :$:", principle)
print("Interest Rate: %", interestrate)
print("Total Frst year of interest: $ ", firstyearinterest)
