
r = input ("Do you want to run the program? yes or no?  ")


while r == 'yes':
  make = input ("Enter make:  ")
  model = input ("model:  ")
  msrp = int(input ("Enter MSRP:  "))
  if make == 'Honda' and model == 'Accord':
    percentoff = 0.10
  elif make == 'Toyota' and model == 'Rav 4':
    percentoff = 0.15
  else:
    percentoff = 0.05
  discount = msrp * percentoff
  discounttotal = msrp - discount
  tax = discounttotal * 0.07
  sum = (msrp - discount) + tax
  print ("The Discount total is:$  ", discounttotal)
  print ("The Sum of all sales is :$ ", sum)
  r = input ("Do you want to run the program? yes or no?  ")