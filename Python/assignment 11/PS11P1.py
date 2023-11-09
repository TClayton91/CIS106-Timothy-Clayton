def discount(qty,price,discrate):
  total = (qty * price)
  discamt = discrate * total
  discprice = total - discamt
  
  return discprice,discamt

qty = int(input("Enter quantity: "))
price = int(input("Enter price: "))
discrate = float(input("Enter discount rate: "))
discamt,discprice = discount(qty,price,discrate)

print("Quantity:           ",qty)
print("Unit Price:$        ",price)
print("Discounted Amount:$ ",discamt)
print(" Discounted Price:$ ",discprice)