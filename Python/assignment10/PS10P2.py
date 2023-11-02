
r = input ("Do you want to run the program? yes or no?  ")

gallonspaintneeded = 0.0

while r == 'yes':
  length = int(input ("Enter Length:  "))
  width = int(input ("Enter Width:  "))
  height = int(input ("Enter Height:  "))
  squarefootage = (2 * length * width) + (2 * length * height)+ (2 * width * height) 
  gallonspaintneeded  = squarefootage / 50
  print ("Square Footage", squarefootage)
  print ("Gallons of Paint Needed:  ", gallonspaintneeded)
  r = input ("Do you want to run the program? yes or no?  ")