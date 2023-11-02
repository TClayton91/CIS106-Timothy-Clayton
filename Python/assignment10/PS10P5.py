
r = input ("Do you want to run the program? yes or no?  ")
totalmarketvalue = 0
totalassessedvalue = 0
while r == 'yes':
  county = input ("Enter County You live in:  ")
  marketvalue = int(input ("Enter Market Value of Home:  "))
                          
  if county == 'Cook':
    assessedvalueper = 0.90
  elif county == 'DuPage':
    assessedvalueper = 0.80
  elif county == 'McHenry':
    assessedvalueper = 0.75
  elif county == 'Kane':
    assedvalueper = 0.60
  else:
    assessedvalueper = 0.70
  
  assessedvalue = marketvalue * assedvalueper
  totalmarketvalue = totalmarketvalue + marketvalue
  totalassessedvalue = totalassessedvalue + assessedvalue
  print ("The assessed value of your home is:$  ", assessedvalue)
  print ("The Marktet Value of your home  is:$  ", marketvalue)

  r = input ("Do you want to run the program? yes or no?  ")   


print ("Total Sum of All Market Values", totalmarketvalue)
print ("Total Sum of All Assessed Values", totalassessedvalue)