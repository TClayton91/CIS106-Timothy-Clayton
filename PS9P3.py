
def mpg(miles, gallons):
  mpg = miles // gallons

numberofcities = 0.0
r = input("Do you want to compute mpg (y/n?")

while r == 'y':
  destination = input("Enter Destination: ")
  miles = float(input("Enter Miles: "))
  gallons = float(input("Enter Gallons Used: "))
  mpg = miles / gallons
  numberofcities = numberofcities+ 1
  print("Miles Per Gallon is:", mpg)
  r = input("Do you want to compute mpg (y/n?")

print("Total Number of Cities: ", numberofcities)