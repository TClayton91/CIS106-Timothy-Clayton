nextmonthforcast = 0.0

r = input ("Do you want to run this program? yes or no?")

while r == 'yes':
  lastname = input ("Enter Last Name:  ")
  month = input ("Enter Month:  ")
  sales = input ("Enter Sales:  ")

if (month == 'Jan''Feb''Mar'):
  forecastper = 0.10
elif (month == 'Apr''May''Jun'):
  forecastper = 0.15
elif (month == 'Jul''Aug''Sep'):
  forecastper = 0.20
elif (month == 'Oct''Nov''Dec'):
    forecastper = 0.25


nextmonthforcast = sales * (1 + forecastper)
r = input ("Do you want to run this program? yes or no?")


print ("Next Month Sales:$  ", nextmonthforcast)
