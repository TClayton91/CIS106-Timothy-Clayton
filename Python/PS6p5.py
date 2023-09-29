employeelastname = input("Enter Employee Last Name")
salary = float(input("Enter Salary :$"))
joblevel = float(input("Enter Job Level"))

if joblevel >= 10:
  bonusrate = 0.25
elif joblevel>= 5 or numberoftickets <= 9:
  bonusrate = 0.20
else:
  bonusrate = 0.10

bonus = salary * bonusrate

print("Last Name",employeelastname)
print("Bonus",bonus)