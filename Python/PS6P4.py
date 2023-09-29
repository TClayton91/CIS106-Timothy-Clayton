numberofticket = float(input("Enter Number of Tickets"))

if numberofticket >= 25:
  priceperticket = 50
elif numberofticket>= 10 or numberoftickets <= 24:
  priceperticket = 60
elif numberofticket >= 5 or numberofticket <=9:
  priceperticket =  70
else:
  priceperticket = 75

total = numberofticket * priceperticket

print("Number of Tickets Purchased:",numberofticket)
print("Price Per Ticket",priceperticket)
print("Total Cost",total)