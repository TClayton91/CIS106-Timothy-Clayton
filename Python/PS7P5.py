numberoforders = 0
sumofdiscamt = 0

response = input("Do you want to calculate yoru toal order with discount? (Yes or No)")

while response == "Yes":
  numberoforders = numberoforders + 1
  qty = float(input("enter Number of Quantity"))
  price = float(input("Enter price"))
  extprice = qty * price

  if extprice >= 10000.00:
  discountamount = extprice * 0.25
  else:
  discountamount = extprice * 0.10
  response = input("Do you want to calculate yoru toal   order with discount? (Yes or No)")

totalorder = extprice - discountamount
sumofdiscamt = sumofdiscamt + discountamount
numberoforders= numberoforders + 1

print("Extended Prince is :$ ",extprice)
print("Discount earned :$" & discountamount)
print("Total Order Amount" & totalorder)
