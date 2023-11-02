
r = input ("Do you want to run the program? yes or no?  ")
sumofticketsbought = 0
ticketsbought = 0
while r == 'yes':
  lastname = input ("Enter Last Name:  ")
  milesfromdwntwnchicago = int(input ("Enter number of miles from Downtown Chicago:  "))
                          
  if milesfromdwntwnchicago >= 30:
    ticketprice = 12
  elif milesfromdwntwnchicago >20 and milesfromdwntwnchicago <29:
    ticketprice = 10
  elif milesfromdwntwnchicago >10 and milesfromdwntwnchicago <19:
    ticketprice = 8
  else:
    ticketprice = 5

  
  numoftickets = ticketsbought + 1
  sumofticketsbought = ticketprice + ticketprice

  print ("The ticket price is: ", ticketprice)

  r = input ("Do you want to run the program? yes or no?  ")   


print ("Total Sum of All tickets", sumofticketsbought)