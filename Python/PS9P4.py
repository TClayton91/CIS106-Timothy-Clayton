def grosspay(hours, rate):
  grosspay = hours * rate

totalgrosspay = 0.0
r = input("Do you want to compute grosspay (y/n?)")

while r == 'y':
  lastname = input("Enter Last Name:" )
  hours = float(input("Enter Hours: "))
  totalgrosspay = totalgrosspay =  grosspay


  
  jobcode = (input("job code: "))
  if (jobcode == 'L' ):
    rate = 25.00
  elif (jobcode == 'A'):
    rate = 30.00
  elif (jobcode == 'J'):
    rate = 50.00
  
 
  grosspay = hours * rate
  totalgrosspay = totalgrosspay + grosspay
  print("Grosspay is: ", grosspay)
  r = input("Do you want to compute grosspay (y/n?")

print("Total Grosspay: ", totalgrosspay)

