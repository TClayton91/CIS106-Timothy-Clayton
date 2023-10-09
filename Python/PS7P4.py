sumofgrosspay = 0
numofemployees= 0

response = input("Do you want to compute the gross pay?")

while response == "Yes":
  numofemployees = numofemployees + 1
  lastname = input("Enter Last Name")
  hoursworked = float(input("Enter Hours Worked"))
  rateofpay = float(input("Enter Rate of Pay"))
  if hoursworked >= 40:
    float(input(grosspay = (40 * rateofpay) + (hours - 40) * 1.5 * rateofpay))
  else:
    grosspay = rateofpay * hoursworked
sumofgrosspay = sumofgrosspay + grosspay
numofemployees = numofemployees + 1

print("Sum of all gross pay is $", sumofgrosspay)
print("Number of employees is :", numofemployees)
