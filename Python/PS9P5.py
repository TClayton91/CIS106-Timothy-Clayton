def tuitioncost(credithours, costpercredithour):
  credithours * costpercredithour

totaltuitioncost = 0.0
r = input("Do you want to compute tuition cost (y/n?)")
while r == 'y':
  lastname = input("Enter Last Name:" )
  credithours = float(input("Enter Credit Hours: "))
  
  districtcode = (input("Enter District Code: "))
  if (districtcode == 'I' ):
    costpercredithour = 250.00
  elif (districtcode == 'O'):
    costpercredithour = 550.00
 
  tuitioncost = credithours * costpercredithour
  totaltuitioncost = totaltuitioncost + tuitioncost
  print("Last Name:  ", lastname)
  print("Tuition Owed", tuitioncost)
  r = input("Do you want to compute tuition cost (y/n?)")


print("Total Tuition Cost: ", totaltuitioncost)